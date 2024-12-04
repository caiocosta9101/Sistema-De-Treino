import mysql.connector
from datetime import datetime

# Configuração da conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',  # Coloque o seu usuário do mysql
    password='1234',  # Coloque a sua senha do mysql
    database='musculacao'  # Coloque sua base de dados do mysql
)

# Função para exibir uma linha decorativa
def exibir_linha():
    print("=" * 50)

# Função para exibir o menu principal do sistema
def exibir_menu_principal():
    exibir_linha()
    print("Sistema de Gerenciamento de Treino".center(50))
    exibir_linha()
    print("[1] Cadastrar Usuário")
    print("[2] Login")
    print("[3] Sair")
    exibir_linha()

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    exibir_linha()
    print("Cadastro de Usuário".center(50))
    exibir_linha()

    # Verificação do nome
    while True:
        nome = input("Digite seu nome: ").strip()
        if nome:
            break
        print("Erro: O nome não pode estar vazio.")

    # Verificação do e-mail
    while True:
        email = input("Digite seu e-mail: ").strip()
        if '@' in email and '.' in email:
            break
        print("Erro: O e-mail deve conter '@' e '.'")

    # Verificação da senha
    while True:
        senha = input("Digite sua senha: ").strip()
        if len(senha) >= 8:
            break
        print("Erro: A senha deve conter pelo menos 8 caracteres.")

    # Verificação da idade
    idade = obter_numero_positivo("Digite sua idade: ")

    # Inserindo o novo usuário no banco de dados
    try:
        cursor = conexao.cursor()
        sql = 'INSERT INTO usuarios (nome, email, senha, idade) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, (nome, email, senha, idade))
        conexao.commit()
        cursor.close()
        print("Usuário cadastrado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar usuário: {err}")


# Função para realizar o login do usuário
def login_usuario():
    exibir_linha()
    print("LOGIN".center(50))
    exibir_linha()

    while True:
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite sua senha: ").strip()
# verificando se o login existe dentro do banco de dados 
        try:
            cursor = conexao.cursor()
            sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
            cursor.execute(sql, (email, senha))
            usuario = cursor.fetchone()
            cursor.close()

            if usuario:
                print("Login realizado com sucesso!")
                return usuario
            else:
                print("Erro: E-mail ou senha incorretos.")
                if not tentar_novamente_ou_sair():
                    return None
        except mysql.connector.Error as err:
            print(f"Erro ao realizar login: {err}")
            break


# Função para exibir o menu do usuário logado
def exibir_menu_usuario():
    exibir_linha()
    print("MENU DO USUÁRIO".center(50))
    exibir_linha()
    print("[1] Gerenciar Treinos")
    print("[2] Registrar Progresso")
    print("[3] Visualizar Histórico de Progresso")
    print("[4] Gerenciar Perfil")
    print("[5] Sair")
    exibir_linha()

# Função para o menu do usuário logado
def menu_usuario_logado(usuario):
    id_usuario = usuario[0]  
    
    while True:
        exibir_menu_usuario()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            gerenciar_treinos(id_usuario) 
        elif opcao == '2':
            registrar_progresso(id_usuario)
        elif opcao == '3':
            visualizar_historico(id_usuario)
        elif opcao == '4':
            print("Opção: Gerenciar Perfil")
            # Lógica para gerenciar perfil
        elif opcao == '5':
            print("Saindo do menu do usuário...")
            break  # Retorna ao menu principal
        else:
            print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
            pausar_para_continuar()


# Função para exibir o submenu de gerenciamento de treinos
def exibir_menu_gerenciar_treinos():
    exibir_linha()
    print("GERENCIAR TREINOS".center(50))
    exibir_linha()
    print("[1] Criar Novo Treino")
    print("[2] Listar Treinos Existentes")
    print("[3] Editar Treino")
    print("[4] Remover Treino")
    print("[5] Voltar")
    exibir_linha()

def gerenciar_treinos(id_usuario):
    while True:
        exibir_menu_gerenciar_treinos()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            criar_novo_treino(id_usuario)
        elif opcao == '2':
            retorno = listar_treinos(id_usuario)
            if retorno == 'menu':
                break
        elif opcao == '3':
            editar_treino(id_usuario)
        elif opcao == '4':
            remover_treino(id_usuario)
        elif opcao == '5':
            print("Voltando ao menu principal...")
            break
        else:
            print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
            pausar_para_continuar()

def criar_novo_treino(id_usuario):
    exibir_linha()
    print("Criar Novo Treino".center(50))
    exibir_linha()

    # Solicitar o nome do treino
    nome_treino = input("Digite o nome do treino: ").strip()
    if not nome_treino:
        print("Erro: O nome do treino não pode ser vazio.")
        return

    # Escolher a periodização
    while True:
        print("\nEscolha uma periodização para o treino:")
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT idperiodizacao, nome FROM periodizacao")
                periodizacoes = cursor.fetchall()

                if not periodizacoes:
                    print("Nenhuma periodização encontrada. Cadastre uma periodização antes de criar o treino.")
                    return

                for idx, periodizacao in enumerate(periodizacoes, start=1):
                    print(f"[{idx}] {periodizacao[1]}")

                escolha_periodizacao = input("Digite o número da periodização desejada: ").strip()
                if escolha_periodizacao.isdigit() and int(escolha_periodizacao) in range(1, len(periodizacoes) + 1):
                    id_periodizacao = periodizacoes[int(escolha_periodizacao) - 1][0]
                    break
                print("Escolha inválida. Tente novamente.")
        except mysql.connector.Error as err:
            print(f"Erro ao obter periodizações: {err}")
            return

    # Inserir o treino na tabela Treinos
    try:
        with conexao.cursor() as cursor:
            sql_treino = "INSERT INTO treinos (id_usuario, id_periodizacao, nome) VALUES (%s, %s, %s)"
            cursor.execute(sql_treino, (id_usuario, id_periodizacao, nome_treino))
            conexao.commit()
            id_treino = cursor.lastrowid
            print("Treino criado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar treino: {err}")
        return

    # Adicionar exercícios ao treino
    while True:
        exibir_linha()
        print("Adicionar Exercício ao Treino".center(50))
        exibir_linha()

        # Mostrar grupos musculares
        grupos = ["Peitoral", "Costas", "Pernas", "Ombros", "Bíceps", "Tríceps", "Abdômen"]
        for idx, grupo in enumerate(grupos, start=1):
            print(f"[{idx}] {grupo}")
        print("[8] Voltar")
        exibir_linha()

        escolha_grupo = input("Digite o número do grupo muscular ou '8' para voltar: ").strip()
        if escolha_grupo == '8':
            print("Voltando ao menu principal...")
            break
        if not escolha_grupo.isdigit() or int(escolha_grupo) not in range(1, len(grupos) + 1):
            print("Escolha inválida. Tente novamente.")
            continue

        grupo_selecionado = grupos[int(escolha_grupo) - 1]
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT idexercicio, nome FROM exercicios WHERE grupo_muscular = %s"
                cursor.execute(sql, (grupo_selecionado,))
                exercicios = cursor.fetchall()

                if not exercicios:
                    print(f"Nenhum exercício encontrado para o grupo muscular {grupo_selecionado}.")
                    continue

                print(f"\nExercícios do grupo muscular {grupo_selecionado}:")
                for idx, exercicio in enumerate(exercicios, start=1):
                    print(f"[{idx}] {exercicio[1]}")
                print("[0] Voltar")

            while True:
                escolha_exercicio = input("Digite o número do exercício desejado ou '0' para voltar: ").strip()
                if escolha_exercicio == '0':
                    break
                if not escolha_exercicio.isdigit() or int(escolha_exercicio) not in range(1, len(exercicios) + 1):
                    print("Escolha inválida. Tente novamente.")
                    continue

                # Selecionar o exercício escolhido
                id_exercicio = exercicios[int(escolha_exercicio) - 1][0]

                # Solicitar detalhes do exercício
                numero_series = obter_numero_positivo("Digite o número de séries: ")
                
                mesmo_detalhes = None
                if numero_series > 1:
                    mesmo_detalhes = validar_sim_nao("As séries terão as mesmas configurações de carga e repetições? (s/n): ")

                repeticoes_previas, carga_previa = None, None

                if mesmo_detalhes == 's':
                    # Solicitar configurações uma vez
                    print(f"\nConfiguração para todas as {numero_series} séries:")
                    repeticoes_previas = obter_numero_positivo("Número de repetições: ")
                    carga_previa = obter_numero_positivo("Carga utilizada (kg): ")

                    # Inserir todas as séries no banco
                    try:
                        with conexao.cursor() as cursor:
                            sql_detalhe = """
                                INSERT INTO treinodetalhes (id_treino, id_exercicio, series, repeticoes, carga)
                                VALUES (%s, %s, %s, %s, %s)
                            """
                            for serie in range(1, numero_series + 1):
                                cursor.execute(sql_detalhe, (id_treino, id_exercicio, serie, repeticoes_previas, carga_previa))
                            conexao.commit()
                            print(f"{numero_series} série(s) configurada(s) com sucesso!")
                    except mysql.connector.Error as err:
                        print(f"Erro ao adicionar série ao treino: {err}")
                        return
                else:
                    # Solicitar configurações para cada série individualmente
                    for serie in range(1, numero_series + 1):
                        print(f"\nConfiguração da Série {serie}:")
                        repeticoes = obter_numero_positivo(f"Número de repetições para a Série {serie}: ")
                        carga = obter_numero_positivo(f"Carga utilizada (kg) para a Série {serie}: ")

                        # Inserir no banco
                        try:
                            with conexao.cursor() as cursor:
                                sql_detalhe = """
                                    INSERT INTO treinodetalhes (id_treino, id_exercicio, series, repeticoes, carga)
                                    VALUES (%s, %s, %s, %s, %s)
                                """
                                cursor.execute(sql_detalhe, (id_treino, id_exercicio, serie, repeticoes, carga))
                                conexao.commit()
                        except mysql.connector.Error as err:
                            print(f"Erro ao adicionar série ao treino: {err}")
                            return

                    print(f"{numero_series} série(s) configurada(s) para o exercício!")
        except mysql.connector.Error as err:
            print(f"Erro ao obter exercícios: {err}")




        
def listar_treinos(id_usuario):
    while True:
        exibir_linha()
        print("Lista de Treinos".center(50))
        exibir_linha()
        
        try:
            cursor = conexao.cursor()
            sql_treinos = """
                SELECT t.idtreino, t.nome, p.nome AS periodizacao
                FROM treinos t
                JOIN periodizacao p ON t.id_periodizacao = p.idperiodizacao
                WHERE t.id_usuario = %s
            """
            cursor.execute(sql_treinos, (id_usuario,))
            treinos = cursor.fetchall()

            if not treinos:
                print("Nenhum treino encontrado.")
                return

            print("Selecione um treino para ver os detalhes:")
            print("-" * 50)
            for i, treino in enumerate(treinos, start=1):
                print(f"[{i}] {treino[1]} (Periodização: {treino[2]})")
            print("-" * 50)

            escolha = input("Digite o número do treino ou 'voltar' para o menu de gerenciamento de treinos: ").strip().lower()
            if escolha == 'voltar':
                return
            if escolha.isdigit() and 1 <= int(escolha) <= len(treinos):
                id_treino, nome_treino, periodizacao = treinos[int(escolha) - 1]
            else:
                print("Opção inválida. Por favor, digite o número do treino ou 'voltar'.")
                continue

            # Exibir detalhes do treino selecionado
            while True:
                print(f"\nTreino: {nome_treino} (Periodização: {periodizacao})")
                print("-" * 65)

                sql_exercicios = """
                    SELECT e.nome, td.series, td.repeticoes, td.carga
                    FROM treinodetalhes td
                    JOIN exercicios e ON td.id_exercicio = e.idexercicio
                    WHERE td.id_treino = %s
                """
                cursor.execute(sql_exercicios, (id_treino,))
                exercicios = cursor.fetchall()

                if not exercicios:
                    print("Nenhum exercício encontrado para este treino.")
                else:
                    print(f"{'Exercício':<30} | {'Séries':>6} | {'Repetições':>12} | {'Carga (kg)':>10}")
                    print("-" * 65)
                    for nome_exercicio, series, repeticoes, carga in exercicios:
                        print(f"{nome_exercicio:<30} | {series:>6} | {repeticoes:>12} | {carga:>10.1f}")
                print("-" * 65)

                escolha_detalhe = input("\nPressione 'voltar' para retornar à lista de treinos ou 'sair' para o menu de gerenciamento de treinos: ").strip().lower()
                if escolha_detalhe == 'sair':
                    return
                elif escolha_detalhe == 'voltar':
                    break
                else:
                    print("Opção inválida. Por favor, digite 'voltar' ou 'sair'.")
        except mysql.connector.Error as err:
            print(f"Erro ao listar treinos: {err}")
        finally:
            cursor.close()



# Função para editar um treino
def editar_treino(id_usuario):
    exibir_linha()
    print("Editar Treino".center(50))
    exibir_linha()
    
    # Exibir lista de treinos para o usuário escolher
    try:
        cursor = conexao.cursor()
        sql_treinos = """
            SELECT idtreino, nome
            FROM treinos
            WHERE id_usuario = %s
        """
        cursor.execute(sql_treinos, (id_usuario,))
        treinos = cursor.fetchall()
        
        if not treinos:
            print("Nenhum treino encontrado para editar.")
            return  # Volta ao menu anterior

        # Exibir os treinos disponíveis
        for idx, treino in enumerate(treinos, start=1):
            print(f"[{idx}] {treino[1]}")

        while True:
            escolha = input("Digite o número do treino que deseja editar (ou 'voltar' para sair): ").strip().lower()
            
            if escolha == 'voltar':
                print("Voltando ao menu de gerenciamento de treinos...")
                return  # Volta ao menu de gerenciamento

            if escolha.isdigit() and 1 <= int(escolha) <= len(treinos):
                id_treino = treinos[int(escolha) - 1][0]
                break
            else:
                print("Escolha inválida. Digite um número válido ou 'voltar' para sair.")

    except mysql.connector.Error as err:
        print(f"Erro ao buscar treinos: {err}")
        return
    finally:
        cursor.close()
    
    # Menu de opções para edição do treino
    while True:
        exibir_linha()
        print("Opções de Edição".center(50))
        exibir_linha()
        print("[1] Alterar Nome do Treino")
        print("[2] Alterar Periodização")
        print("[3] Adicionar Exercíco")
        print("[4] Remover Exercício")
        print("[5] Voltar")
        exibir_linha()
        
        opcao = input("Escolha a opção desejada: ").strip()
        if opcao == '1':
    # Editar Nome do Treino
            while True:
                novo_nome = input("Digite o novo nome do treino: ").strip()
                if novo_nome:  # Verifica se o nome não está vazio
                    try:
                        cursor = conexao.cursor()
                        cursor.execute("UPDATE treinos SET nome = %s WHERE idtreino = %s", (novo_nome, id_treino))
                        conexao.commit()
                        print("Nome do treino atualizado com sucesso!")
                        break  # Sai do loop após o sucesso
                    except mysql.connector.Error as err:
                        print(f"Erro ao atualizar o nome do treino: {err}")
                    finally:
                        cursor.close()
                else:
                    print("Erro: O nome do treino não pode ser vazio. Tente novamente.")
                
        elif opcao == '2':
    # Editar Periodização
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT idperiodizacao, nome FROM periodizacao")
                periodizacoes = cursor.fetchall()
                cursor.close()
        
                if not periodizacoes:
                    print("Nenhuma periodização disponível para selecionar.")
                    continue
        
                print("Escolha uma nova periodização:")
                for idx, periodizacao in enumerate(periodizacoes, start=1):
                    print(f"[{idx}] {periodizacao[1]}")
        
                while True:
                    escolha_periodizacao = input("Digite o número da nova periodização: ").strip()
                    if escolha_periodizacao.isdigit() and 1 <= int(escolha_periodizacao) <= len(periodizacoes):
                        id_periodizacao = periodizacoes[int(escolha_periodizacao) - 1][0]
                        try:
                            cursor = conexao.cursor()
                            cursor.execute("UPDATE treinos SET id_periodizacao = %s WHERE idtreino = %s", (id_periodizacao, id_treino))
                            conexao.commit()
                            cursor.close()
                            print("Periodização atualizada com sucesso!")
                            break
                        except mysql.connector.Error as err:
                            print(f"Erro ao atualizar a periodização: {err}")
                            break
                    else:
                        print("Escolha inválida. Digite um número válido da lista.")
    
            except mysql.connector.Error as err:
                print(f"Erro ao buscar periodizações: {err}")

        elif opcao == '3':
            # Modificar Exercícios (adicionar/excluir novamente)
            adicionar_exercicios(id_treino)
        elif opcao == '4':
            # Remover um Exercício do Treino
            remover_exercicios(id_treino)
        elif opcao == '5':
            print("Voltando ao menu de gerenciamento de treinos...")
            break
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

# Função para adicionar exercícios ao treino
def adicionar_exercicios(id_treino):
    while True:
        exibir_linha()
        print("Adicionar Exercício ao Treino".center(50))
        exibir_linha()

        # Mostrar grupos musculares
        grupos = ["Peitoral", "Costas", "Pernas", "Ombros", "Bíceps", "Tríceps", "Abdômen"]
        for idx, grupo in enumerate(grupos, start=1):
            print(f"[{idx}] {grupo}")
        print("[8] Voltar")
        exibir_linha()

        escolha_grupo = input("Digite o número do grupo muscular ou '8' para voltar: ").strip()
        if escolha_grupo == '8':
            print("Voltando ao menu de gerenciamento de treinos...")
            return
        if not escolha_grupo.isdigit() or int(escolha_grupo) not in range(1, len(grupos) + 1):
            print("Escolha inválida. Tente novamente.")
            continue

        # Selecionar exercícios do grupo muscular escolhido
        grupo_selecionado = grupos[int(escolha_grupo) - 1]
        try:
            with conexao.cursor() as cursor:
                sql = "SELECT idexercicio, nome FROM exercicios WHERE grupo_muscular = %s"
                cursor.execute(sql, (grupo_selecionado,))
                exercicios = cursor.fetchall()

                if not exercicios:
                    print(f"Nenhum exercício encontrado para o grupo muscular {grupo_selecionado}.")
                    continue

                print(f"\nExercícios do grupo muscular {grupo_selecionado}:")
                for idx, exercicio in enumerate(exercicios, start=1):
                    print(f"[{idx}] {exercicio[1]}")
                print("[0] Voltar")

            while True:
                escolha_exercicio = input("Digite o número do exercício desejado ou '0' para voltar: ").strip()
                if escolha_exercicio == '0':
                    break
                if not escolha_exercicio.isdigit() or int(escolha_exercicio) not in range(1, len(exercicios) + 1):
                    print("Escolha inválida. Tente novamente.")
                    continue

                # Selecionar o exercício escolhido
                id_exercicio = exercicios[int(escolha_exercicio) - 1][0]

                # Solicitar detalhes do exercício
                numero_series = obter_numero_positivo("Digite o número de séries: ")
                
                mesmo_detalhes = None
                if numero_series > 1:
                    mesmo_detalhes = validar_sim_nao("As séries terão as mesmas configurações de carga e repetições? (s/n): ")

                repeticoes_previas, carga_previa = None, None

                if mesmo_detalhes == 's':
                    # Solicitar configurações uma vez
                    print(f"\nConfiguração para todas as {numero_series} séries:")
                    repeticoes_previas = obter_numero_positivo("Número de repetições: ")
                    carga_previa = obter_numero_positivo("Carga utilizada (kg): ")

                    # Inserir todas as séries no banco
                    try:
                        with conexao.cursor() as cursor:
                            sql_detalhe = """
                                INSERT INTO treinodetalhes (id_treino, id_exercicio, series, repeticoes, carga)
                                VALUES (%s, %s, %s, %s, %s)
                            """
                            for serie in range(1, numero_series + 1):
                                cursor.execute(sql_detalhe, (id_treino, id_exercicio, serie, repeticoes_previas, carga_previa))
                            conexao.commit()
                            print(f"{numero_series} série(s) configurada(s) com sucesso!")
                    except mysql.connector.Error as err:
                        print(f"Erro ao adicionar série ao treino: {err}")
                        return
                else:
                    # Solicitar configurações para cada série individualmente
                    for serie in range(1, numero_series + 1):
                        print(f"\nConfiguração da Série {serie}:")
                        repeticoes = obter_numero_positivo(f"Número de repetições para a Série {serie}: ")
                        carga = obter_numero_positivo(f"Carga utilizada (kg) para a Série {serie}: ")

                        # Inserir no banco
                        try:
                            with conexao.cursor() as cursor:
                                sql_detalhe = """
                                    INSERT INTO treinodetalhes (id_treino, id_exercicio, series, repeticoes, carga)
                                    VALUES (%s, %s, %s, %s, %s)
                                """
                                cursor.execute(sql_detalhe, (id_treino, id_exercicio, serie, repeticoes, carga))
                                conexao.commit()
                        except mysql.connector.Error as err:
                            print(f"Erro ao adicionar série ao treino: {err}")
                            return

                    print(f"{numero_series} série(s) configurada(s) para o exercício!")

                # Perguntar se deseja adicionar mais exercícios
                adicionar_mais = validar_sim_nao("Deseja adicionar outro exercício ao mesmo grupo? (s/n): ")
                if adicionar_mais.lower() == 'n':
                    print("Voltando ao menu principal...")
                    break

        except mysql.connector.Error as err:
            print(f"Erro ao obter exercícios: {err}")
            return


# Função para remover exercícios de um treino
def remover_exercicios(id_treino):
    exibir_linha()
    print("Remover Exercício".center(50))
    exibir_linha()
    
    try:
        cursor = conexao.cursor()

        # Buscar os exercícios associados ao treino
        sql_exercicios = """
            SELECT DISTINCT e.idexercicio, e.nome
            FROM treinodetalhes td
            JOIN exercicios e ON td.id_exercicio = e.idexercicio
            WHERE td.id_treino = %s
        """
        cursor.execute(sql_exercicios, (id_treino,))
        exercicios = cursor.fetchall()

        if not exercicios:
            print("Nenhum exercício encontrado para remover.")
            return

        while True:  # Mantém o loop para continuar removendo exercícios
            # Exibir a lista de exercícios
            print("\nExercícios no treino:")
            for idx, (id_exercicio, nome_exercicio) in enumerate(exercicios, start=1):
                print(f"[{idx}] {nome_exercicio}")

            # Escolher o exercício para remover
            escolha = input("Digite o número do exercício que deseja remover ou 'voltar' para sair: ").strip().lower()
            
            if escolha == 'voltar':
                print("Voltando ao menu anterior...")
                break

            if escolha.isdigit() and 1 <= int(escolha) <= len(exercicios):
                id_exercicio = exercicios[int(escolha) - 1][0]
                nome_exercicio = exercicios[int(escolha) - 1][1]
            else:
                print("Escolha inválida. Por favor, digite um número válido ou 'voltar'.")
                continue

            # Confirmar a remoção
            confirmacao = validar_sim_nao(f"Tem certeza de que deseja remover o exercício '{nome_exercicio}'? (s/n): ")
            if confirmacao == 's':
                try:
                    # Remover todas as séries do exercício selecionado para o treino
                    cursor.execute("DELETE FROM treinodetalhes WHERE id_treino = %s AND id_exercicio = %s", (id_treino, id_exercicio))
                    conexao.commit()
                    print(f"Exercício '{nome_exercicio}' removido com sucesso!")
                    
                    # Atualizar a lista de exercícios após remoção
                    cursor.execute(sql_exercicios, (id_treino,))
                    exercicios = cursor.fetchall()

                    if not exercicios:
                        print("Todos os exercícios foram removidos. Voltando ao menu.")
                        break
                except mysql.connector.Error as err:
                    print(f"Erro ao remover exercício: {err}")
            else:
                print("Remoção cancelada.")

            # Perguntar se deseja continuar removendo exercícios
            continuar = validar_sim_nao("Deseja remover outro exercício? (s/n): ")
            if continuar == 'n':
                print("Voltando ao menu anterior...")
                break
    except mysql.connector.Error as err:
        print(f"Erro ao buscar exercícios: {err}")
    finally:
        cursor.close()



#função pra remover os treinos
def remover_treino(id_usuario):
    while True:
        exibir_linha()
        print("Remover Treino".center(50))
        exibir_linha()

        try:
            cursor = conexao.cursor()
            sql_treinos = """
                SELECT idtreino, nome
                FROM treinos
                WHERE id_usuario = %s
            """
            cursor.execute(sql_treinos, (id_usuario,))
            treinos = cursor.fetchall()
            
            if not treinos:
                print("Nenhum treino encontrado.")
                cursor.close()
                return  # Retorna ao menu anterior

            # Exibir lista de treinos
            for idx, (id_treino, nome_treino) in enumerate(treinos, start=1):
                print(f"[{idx}] {nome_treino}")
            print("Digite o número do treino que deseja remover ou 'voltar' para sair:")

            # Entrada do usuário
            escolha = input().strip().lower()
            if escolha == 'voltar':
                print("Voltando ao menu de gerenciamento de treinos...")
                cursor.close()
                break

            if not escolha.isdigit() or not (1 <= int(escolha) <= len(treinos)):
                print("Escolha inválida. Por favor, digite um número válido ou 'voltar'.")
                continue

            id_treino, nome_treino = treinos[int(escolha) - 1]

            # Confirmação de remoção
            confirmacao = input(f"Tem certeza de que deseja remover o treino '{nome_treino}' e todos os seus exercícios? (s/n): ").strip().lower()
            if confirmacao == 's':
                try:
                    # Remover detalhes do treino e o treino em si
                    cursor.execute("DELETE FROM treinodetalhes WHERE id_treino = %s", (id_treino,))
                    cursor.execute("DELETE FROM treinos WHERE idtreino = %s", (id_treino,))
                    conexao.commit()
                    print(f"Treino '{nome_treino}' removido com sucesso!")
                except mysql.connector.Error as err:
                    print(f"Erro ao remover treino: {err}")
                finally:
                    cursor.close()
                break
            elif confirmacao == 'n':
                print("Remoção cancelada.")
                continue
            else:
                print("Escolha inválida. Por favor, digite 's' ou 'n'.")
                continue

        except mysql.connector.Error as err:
            print(f"Erro ao buscar treinos: {err}")
            return

# função pra registrar o progresso

def registrar_progresso(id_usuario):
    exibir_linha()
    print("Registrar Progresso".center(50))
    exibir_linha()

    try:
        with conexao.cursor() as cursor:
            # Listar treinos do usuário
            sql_treinos = "SELECT idtreino, nome FROM treinos WHERE id_usuario = %s"
            cursor.execute(sql_treinos, (id_usuario,))
            treinos = cursor.fetchall()

            if not treinos:
                print("Nenhum treino encontrado. Cadastre um treino primeiro.")
                return

        # Exibir treinos e selecionar
        print("Treinos disponíveis:")
        for idx, (idtreino, nome_treino) in enumerate(treinos, start=1):
            print(f"[{idx}] {nome_treino}")
        escolha_treino = obter_numero_positivo("Escolha o treino: ") - 1

        if escolha_treino not in range(len(treinos)):
            print("Escolha inválida.")
            return

        id_treino = treinos[escolha_treino][0]

        while True:  # Loop para registrar progresso para vários exercícios
            with conexao.cursor() as cursor:
                # Listar exercícios do treino
                sql_exercicios = """
                    SELECT DISTINCT td.id_exercicio, e.nome
                    FROM treinodetalhes td
                    JOIN exercicios e ON td.id_exercicio = e.idexercicio
                    WHERE td.id_treino = %s
                """
                cursor.execute(sql_exercicios, (id_treino,))
                exercicios = cursor.fetchall()

                if not exercicios:
                    print("Nenhum exercício associado ao treino.")
                    return

            # Exibir exercícios e selecionar
            print("\nExercícios do treino:")
            for idx, (id_exercicio, nome_exercicio) in enumerate(exercicios, start=1):
                print(f"[{idx}] {nome_exercicio}")
            escolha_exercicio = obter_numero_positivo("Escolha o exercício: ") - 1

            if escolha_exercicio not in range(len(exercicios)):
                print("Escolha inválida.")
                continue

            id_exercicio = exercicios[escolha_exercicio][0]

            # Inserir progresso
            data = validar_data("Digite a data (DD/MM/YYYY) [pressione ENTER para usar a data atual]: ")
            numero_series = obter_numero_positivo("Quantas séries deseja registrar? ")
            
            mesmo_detalhes = None
            if numero_series > 1:
                mesmo_detalhes = validar_sim_nao("As séries terão as mesmas configurações de carga e repetições? (s/n): ")

            repeticoes_previas, carga_previa = None, None

            for serie in range(1, numero_series + 1):
                print(f"\nRegistro da Série {serie}:")

                if mesmo_detalhes == 's' and serie > 1:
                    repeticoes_progresso = repeticoes_previas
                    carga_progresso = carga_previa
                else:
                    repeticoes_progresso = obter_numero_positivo(f"Número de repetições para a Série {serie}: ")
                    
                    while True:  # Validação da carga
                        try:
                            carga_progresso = float(input(f"Carga utilizada (kg) para a Série {serie}: "))
                            if carga_progresso <= 0:
                                raise ValueError
                            break
                        except ValueError:
                            print("Erro: Por favor, digite um número válido maior que zero.")

                    observacoes = input("Observações (opcional): ").strip()

                    if mesmo_detalhes == 's' and serie == 1:
                        repeticoes_previas = repeticoes_progresso
                        carga_previa = carga_progresso

                # Inserir progresso no banco de dados
                with conexao.cursor() as cursor:
                    sql_progresso = """
                        INSERT INTO progresso 
                        (id_usuario, id_treino, id_exercicio, data, serie_progresso, repeticoes_progresso, carga_progresso, observacoes)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql_progresso, (id_usuario, id_treino, id_exercicio, data, serie, repeticoes_progresso, carga_progresso, observacoes))
                    conexao.commit()

                print(f"Série {serie} registrada com sucesso!")

            continuar_exercicio = validar_sim_nao("Deseja registrar um progresso para outro exercício? (s/n): ")
            if continuar_exercicio.lower() == 'n':
                print("Registro de progresso concluído. Bom treino!")
                break

    except mysql.connector.Error as err:
        print(f"Erro ao registrar progresso: {err}")


    


# Função para visualizar histórico de progresso com datas formatadas
def visualizar_historico(id_usuario):
    exibir_linha()
    print("Histórico de Progresso".center(50))
    exibir_linha()

    try:
        print("Deseja aplicar algum filtro?")
        print("[1] Por treino")
        print("[2] Por período")
        print("[3] Todos os registros")
        filtro = input("Escolha uma opção: ").strip()

        sql_historico = """
            SELECT DATE_FORMAT(p.data, '%d/%m/%Y') AS data_formatada, 
                   t.nome AS treino, e.nome AS exercicio, 
                   p.serie_progresso, p.repeticoes_progresso, p.carga_progresso, p.observacoes
            FROM progresso p
            JOIN treinos t ON p.id_treino = t.idtreino
            JOIN exercicios e ON p.id_exercicio = e.idexercicio
            WHERE p.id_usuario = %s
        """
        params = [id_usuario]

        if filtro == '1':  # Filtrar por treino
            cursor = conexao.cursor()
            cursor.execute("SELECT idtreino, nome FROM treinos WHERE id_usuario = %s", (id_usuario,))
            treinos = cursor.fetchall()
            cursor.close()

            if not treinos:
                print("Nenhum treino encontrado.")
                return

            print("Treinos disponíveis:")
            for idx, (idtreino, nome_treino) in enumerate(treinos, start=1):
                print(f"[{idx}] {nome_treino}")
            escolha_treino = int(input("Escolha o treino: ").strip()) - 1

            if escolha_treino not in range(len(treinos)):
                print("Escolha inválida.")
                return

            id_treino = treinos[escolha_treino][0]
            sql_historico += " AND p.id_treino = %s"
            params.append(id_treino)

        elif filtro == '2':  # Filtrar por período
            data_inicio = converter_data_para_iso(input("Digite a data inicial (DD/MM/YYYY): ").strip())
            data_fim = converter_data_para_iso(input("Digite a data final (DD/MM/YYYY): ").strip())
            sql_historico += " AND p.data BETWEEN %s AND %s"
            params.extend([data_inicio, data_fim])

        sql_historico += " ORDER BY p.data DESC"

        cursor = conexao.cursor()
        cursor.execute(sql_historico, params)
        historico = cursor.fetchall()
        cursor.close()

        if not historico:
            print("Nenhum registro encontrado.")
            return

        print(f"{'Data':<12} {'Treino':<20} {'Exercício':<20} {'Séries':<6} {'Reps':<6} {'Carga (kg)':<10} Observações")
        print("-" * 80)
        for data, treino, exercicio, series, reps, carga, obs in historico:
            print(f"{data:<12} {treino:<20} {exercicio:<20} {series:<6} {reps:<6} {carga:<10.1f} {obs or ''}")

    except mysql.connector.Error as err:
        print(f"Erro ao visualizar histórico: {err}")

# função pra validar a data
def validar_data(mensagem):
    while True:
        data = input(mensagem).strip()
        if not data:  # Caso o usuário pressione ENTER, retorna a data atual
            return datetime.now().strftime('%Y-%m-%d')
        try:
            data_iso = datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
            return data_iso
        except ValueError:
            print("Erro: Data inválida. Use o formato DD/MM/YYYY.")


# Função para garantir entrada de número positivo
def obter_numero_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor > 0:
                return valor  # Retorna o valor se for um número positivo
            else:
                print("Erro: O valor deve ser um número positivo.")
        except ValueError:
            print("Erro: Por favor, digite um número válido")


# Função para verificar se o usuário quer tentar novamente ou sair
def tentar_novamente_ou_sair(mensagem="Pressione 'ENTER' para tentar novamente ou digite 'sair' para voltar ao menu."):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta == 'sair':
            return False
        elif resposta == '':
            return True
        else:
            print("Opção inválida. Pressione 'ENTER' para tentar novamente ou digite 'sair'.")

# Função para pausar a execução e esperar o usuário continuar
def pausar_para_continuar():
    while input("Pressione ENTER para continuar...") != "":
        pass

# função pra aceitar só sim ou não
def validar_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ['s', 'n']:
            return resposta
        print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")




# Loop principal do menu
while True:
    exibir_menu_principal()
    opcao = input("Digite a opção desejada: ").strip()

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        usuario_logado = login_usuario()
        if usuario_logado:
            menu_usuario_logado(usuario_logado)
    elif opcao == '3':
        print("Saindo do sistema...")
        break
    else:
        print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
        pausar_para_continuar()

# Fechando a conexão com o banco de dados
conexao.close()

