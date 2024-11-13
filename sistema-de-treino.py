import mysql.connector

# Configuração da conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='',  # Coloque o seu usuário do mysql
    password='',  # Coloque a sua senha do mysql
    database=''  # Coloque sua base de dados do mysql
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
            gerenciar_treinos(id_usuario)  # Passa o id_usuario corretamente
        elif opcao == '2':
            print("Opção: Registrar Progresso")
            # Lógica para registrar progresso
        elif opcao == '3':
            print("Opção: Visualizar Histórico de Progresso")
            # Lógica para visualizar histórico de progresso
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
            listar_treinos(id_usuario)  
        elif opcao == '3':
            editar_treino(id_usuario)
           
        elif opcao == '4':
            print("Opção: Remover Treino")
            # Lógica para remover um treino
        elif opcao == '5':
            print("Voltando ao menu do usuário...")
            break
        else:
            print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
            pausar_para_continuar()

# Função para criar um novo treino
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
            cursor = conexao.cursor()
            cursor.execute("SELECT idperiodizacao, nome FROM periodizacao")
            periodizacoes = cursor.fetchall()
            cursor.close()

            if not periodizacoes:
                print("Nenhuma periodização encontrada. Cadastre uma periodização antes de criar o treino.")
                return

            for idx, periodizacao in enumerate(periodizacoes, start=1):
                print(f"[{idx}] {periodizacao[1]}")

            escolha_periodizacao = input("Digite o número da periodização desejada: ").strip()
            if not escolha_periodizacao.isdigit() or int(escolha_periodizacao) not in range(1, len(periodizacoes) + 1):
                print("Escolha inválida. Tente novamente.")
                continue

            id_periodizacao = periodizacoes[int(escolha_periodizacao) - 1][0]
            break

        except mysql.connector.Error as err:
            print(f"Erro ao obter periodizações: {err}")
            return

    # Inserir o treino na tabela Treinos
    try:
        cursor = conexao.cursor()
        sql_treino = "INSERT INTO treinos (id_usuario, id_periodizacao, nome) VALUES (%s, %s, %s)"
        cursor.execute(sql_treino, (id_usuario, id_periodizacao, nome_treino))
        conexao.commit()
        id_treino = cursor.lastrowid
        cursor.close()
        print("Treino criado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar treino: {err}")
        return

    # Adicionar exercícios ao treino
    while True:
        exibir_linha()
        print("Adicionar Exercício ao Treino".center(50))
        exibir_linha()

        # Escolher um exercício da tabela Exercicios
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT idexercicio, nome, grupo_muscular FROM exercicios")
            exercicios = cursor.fetchall()
            cursor.close()

            if not exercicios:
                print("Nenhum exercício encontrado. Cadastre exercícios antes de criar um treino.")
                return

            for idx, exercicio in enumerate(exercicios, start=1):
                print(f"[{idx}] {exercicio[1]} - {exercicio[2]}")

            escolha_exercicio = input("Digite o número do exercício desejado: ").strip()
            if not escolha_exercicio.isdigit() or int(escolha_exercicio) not in range(1, len(exercicios) + 1):
                print("Escolha inválida.")
                continue

            id_exercicio = exercicios[int(escolha_exercicio) - 1][0]

        except mysql.connector.Error as err:
            print(f"Erro ao obter exercícios: {err}")
            return

        # Solicitar o número de séries, repetições e carga
        series = obter_numero_positivo("Digite o número de séries: ")
        repeticoes = obter_numero_positivo("Digite o número de repetições: ")
        carga = obter_numero_positivo("Digite a carga (em kg) para cada série: ")

        # Inserir cada série individualmente na tabela TreinoDetalhes
        try:
            cursor = conexao.cursor()
            sql_detalhe = "INSERT INTO treinodetalhes (id_treino, id_exercicio, series, repeticoes, carga) VALUES (%s, %s, %s, %s, %s)"
            for _ in range(series):
                cursor.execute(sql_detalhe, (id_treino, id_exercicio, 1, repeticoes, carga))  # series = 1 para cada linha
            conexao.commit()
            cursor.close()
            print(f"{series} séries adicionadas com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar exercício ao treino: {err}")
            return

        # Perguntar se o usuário deseja adicionar mais exercícios
        while True:
            adicionar_mais = input("Deseja adicionar outro exercício? (s/n): ").strip().lower()
            if adicionar_mais in ['s', 'n']:
                break
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

        if adicionar_mais == 'n':
            print("Treino finalizado.")
            break
        
def listar_treinos(id_usuario):
    exibir_linha()
    print("Lista de Treinos".center(50))
    exibir_linha()
    
    try:
        cursor = conexao.cursor()
        # Consulta todos os treinos do usuário
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
        
        # Para cada treino, exibe os detalhes
        for treino in treinos:
            id_treino, nome_treino, periodizacao = treino
            print(f"\nTreino: {nome_treino} (Periodização: {periodizacao})")
            print("-" * 50)
            
            # Consulta os exercícios associados ao treino
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
                # Cabeçalho para a tabela de exercícios
                print(f"{'Exercício':<20} | {'Séries':<6} | {'Repetições':<12} | {'Carga (kg)':<10}")
                print("-" * 50)
                
                # Exibe os detalhes de cada exercício
                for nome_exercicio, series, repeticoes, carga in exercicios:
                    print(f"{nome_exercicio:<20} | {series:<6} | {repeticoes:<12} | {carga:<10}")
            
            print("-" * 50)
        
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Erro ao listar treinos: {err}")


# Função para editar um treino
def editar_treino(id_usuario):
    exibir_linha()
    print("Editar Treino".center(50))
    exibir_linha()
    
    # Exibir lista de treinos para o usuário escolher
    cursor = conexao.cursor()
    try:
        sql_treinos = """
            SELECT idtreino, nome
            FROM treinos
            WHERE id_usuario = %s
        """
        cursor.execute(sql_treinos, (id_usuario,))
        treinos = cursor.fetchall()
        
        if not treinos:
            print("Nenhum treino encontrado para editar.")
            return

        # Exibir os treinos disponíveis
        for idx, treino in enumerate(treinos, start=1):
            print(f"[{idx}] {treino[1]}")

        escolha = input("Digite o número do treino que deseja editar: ").strip()
        if not escolha.isdigit() or int(escolha) not in range(1, len(treinos) + 1):
            print("Escolha inválida.")
            return

        id_treino = treinos[int(escolha) - 1][0]

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
        print("[3] Modificar Exercícios")
        print("[4] Remover Exercício")
        print("[5] Voltar")
        exibir_linha()
        
        opcao = input("Escolha a opção desejada: ").strip()
        
        if opcao == '1':
            # Editar Nome do Treino
            novo_nome = input("Digite o novo nome do treino: ").strip()
            if novo_nome:
                try:
                    cursor = conexao.cursor()
                    cursor.execute("UPDATE treinos SET nome = %s WHERE idtreino = %s", (novo_nome, id_treino))
                    conexao.commit()
                    print("Nome do treino atualizado com sucesso!")
                except mysql.connector.Error as err:
                    print(f"Erro ao atualizar o nome do treino: {err}")
                finally:
                    cursor.close()
            else:
                print("O nome do treino não pode ser vazio.")

        elif opcao == '2':
            # Editar Periodização
            try:
                cursor = conexao.cursor()
                cursor.execute("SELECT idperiodizacao, nome FROM periodizacao")
                periodizacoes = cursor.fetchall()
                cursor.close()
                
                if not periodizacoes:
                    print("Nenhuma periodização disponível para selecionar.")
                    return
                
                for idx, periodizacao in enumerate(periodizacoes, start=1):
                    print(f"[{idx}] {periodizacao[1]}")
                
                escolha_periodizacao = input("Digite o número da nova periodização: ").strip()
                if escolha_periodizacao.isdigit() and int(escolha_periodizacao) in range(1, len(periodizacoes) + 1):
                    id_periodizacao = periodizacoes[int(escolha_periodizacao) - 1][0]
                    cursor = conexao.cursor()
                    cursor.execute("UPDATE treinos SET id_periodizacao = %s WHERE idtreino = %s", (id_periodizacao, id_treino))
                    conexao.commit()
                    cursor.close()
                    print("Periodização atualizada com sucesso!")
                else:
                    print("Escolha inválida.")
            except mysql.connector.Error as err:
                print(f"Erro ao atualizar a periodização: {err}")

        elif opcao == '3':
            # Modificar Exercícios (excluir e adicionar novamente)
            adicionar_exercicios(id_treino)
        
        elif opcao == '4':
            # Remover um Exercício do Treino
            remover_exercicios(id_treino)

        elif opcao == '5':
            # Voltar ao menu de gerenciamento de treinos
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

        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT idexercicio, nome, grupo_muscular FROM exercicios")
            exercicios = cursor.fetchall()
            cursor.close()

            if not exercicios:
                print("Nenhum exercício encontrado. Cadastre exercícios antes de adicionar.")
                return

            for idx, exercicio in enumerate(exercicios, start=1):
                print(f"[{idx}] {exercicio[1]} - {exercicio[2]}")

            escolha_exercicio = input("Digite o número do exercício desejado: ").strip()
            if not escolha_exercicio.isdigit() or int(escolha_exercicio) not in range(1, len(exercicios) + 1):
                print("Escolha inválida.")
                continue

            id_exercicio = exercicios[int(escolha_exercicio) - 1][0]
        except mysql.connector.Error as err:
            print(f"Erro ao obter exercícios: {err}")
            return

        series = obter_numero_positivo("Digite o número de séries: ")
        repeticoes = obter_numero_positivo("Digite o número de repetições: ")
        carga = obter_numero_positivo("Digite a carga (em kg) para cada série: ")

        try:
            cursor = conexao.cursor()
            sql_detalhe = "INSERT INTO treinodetalhes (id_treino, id_exercicio, series, repeticoes, carga) VALUES (%s, %s, %s, %s, %s)"
            for _ in range(series):
                cursor.execute(sql_detalhe, (id_treino, id_exercicio, 1, repeticoes, carga))
            conexao.commit()
            cursor.close()
            print(f"{series} séries adicionadas com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar exercício ao treino: {err}")
            return

        adicionar_mais = input("Deseja adicionar outro exercício? (s/n): ").strip().lower()
        if adicionar_mais == 'n':
            print("Edição de exercícios concluída.")
            break


# Função para remover exercícios de um treino
def remover_exercicios(id_treino):
    exibir_linha()
    print("Remover Exercício".center(50))
    exibir_linha()
    
    cursor = conexao.cursor()
    try:
        # Buscar exercícios associados ao treino
        sql_exercicios = """
            SELECT td.idtreinodetalhe, e.nome
            FROM treinodetalhes td
            JOIN exercicios e ON td.id_exercicio = e.idexercicio
            WHERE td.id_treino = %s
        """
        cursor.execute(sql_exercicios, (id_treino,))
        exercicios = cursor.fetchall()
        
        if not exercicios:
            print("Nenhum exercício encontrado para remover.")
            return

        # Listar exercícios e solicitar escolha
        for idx, (id_detalhe, nome_exercicio) in enumerate(exercicios, start=1):
            print(f"[{idx}] {nome_exercicio}")

        escolha = input("Digite o número do exercício que deseja remover: ").strip()
        if escolha.isdigit() and int(escolha) in range(1, len(exercicios) + 1):
            id_detalhe = exercicios[int(escolha) - 1][0]
            cursor.execute("DELETE FROM treinodetalhes WHERE idtreinodetalhe = %s", (id_detalhe,))
            conexao.commit()
            print("Exercício removido com sucesso!")
        else:
            print("Escolha inválida.")

    except mysql.connector.Error as err:
        print(f"Erro ao remover exercício: {err}")
    finally:
        cursor.close()





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




