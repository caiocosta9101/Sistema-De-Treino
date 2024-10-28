import mysql.connector

# Configuração da conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='',  # Substitua pelo seu usuário do MySQL
    password='',  # Substitua pela sua senha do MySQL
    database='musculacao'
)

# Menu inicial do programa com interação com o banco de dados
while True:
    print("=" * 50)
    print(" " * 15 + "SISTEMA DE TREINO")
    print("=" * 50)
    print("Escolha uma opção:")
    print("[1] Cadastrar Usuário")
    print("[2] Login")
    print("[3] Sair")
    print("=" * 50)

    opcao = input("Digite a opção desejada: ").strip().lower()

    if opcao == '1':
        print("=" * 50)
        print(" " * 15 + "CADASTRO DE USUÁRIO")
        print("=" * 50)

        voltar = ""

        # Validação do nome
        while True:
            nome = input("Digite seu nome: ").strip()
            if not nome:
                print("Erro: O nome não pode ser vazio.")
                while True:
                    voltar = input(
                        "Pressione ENTER para tentar novamente ou digite 'sair' para voltar ao menu: ").strip().lower()
                    if voltar == "sair":
                        break
                    elif voltar == "":
                        break
                    else:
                        print("Entrada inválida. Digite 'sair' ou pressione apenas ENTER para tentar novamente.")
            else:
                break

            if voltar == "sair":
                break  # Sai da validação do nome

        if voltar == "sair":
            continue  # Retorna ao menu principal

        # Validação do e-mail
        while True:
            email = input("Digite seu e-mail: ").strip()
            if "@" not in email or "." not in email:
                print("Erro: O e-mail deve conter '@' e '.'")
                while True:
                    voltar = input(
                        "Pressione ENTER para tentar novamente ou digite 'sair' para voltar ao menu: ").strip().lower()
                    if voltar == "sair":
                        break
                    elif voltar == "":
                        break
                    else:
                        print("Entrada inválida. Digite 'sair' ou pressione apenas ENTER para tentar novamente.")
            else:
                break

            if voltar == "sair":
                break  # Sai da validação do e-mail

        if voltar == "sair":
            continue  # Retorna ao menu principal

        # Validação da senha
        while True:
            senha = input("Digite sua senha: ").strip()
            if len(senha) < 8:
                print("Erro: A senha deve ter pelo menos 8 caracteres.")
                while True:
                    voltar = input(
                        "Pressione ENTER para tentar novamente ou digite 'sair' para voltar ao menu: ").strip().lower()
                    if voltar == "sair":
                        break
                    elif voltar == "":
                        break
                    else:
                        print("Entrada inválida. Digite 'sair' ou pressione apenas ENTER para tentar novamente.")
            else:
                break

            if voltar == "sair":
                break  # Sai da validação da senha

        if voltar == "sair":
            continue  # Retorna ao menu principal

        # Validação da idade
        while True:
            try:
                idade = int(input("Digite sua idade: ").strip())
                if idade <= 0:
                    print("Erro: A idade deve ser um número positivo.")
                    while True:
                        voltar = input(
                            "Pressione ENTER para tentar novamente ou digite 'sair' para voltar ao menu: ").strip().lower()
                        if voltar == "sair":
                            break
                        elif voltar == "":
                            break
                        else:
                            print("Entrada inválida. Digite 'sair' ou pressione apenas ENTER para tentar novamente.")
                else:
                    break
            except ValueError:
                print("Erro: A idade deve conter apenas números.")
                while True:
                    voltar = input(
                        "Pressione ENTER para tentar novamente ou digite 'sair' para voltar ao menu: ").strip().lower()
                    if voltar == "sair":
                        break
                    elif voltar == "":
                        break
                    else:
                        print("Entrada inválida. Digite 'sair' ou pressione apenas ENTER para tentar novamente.")

            if voltar == "sair":
                break  # Sai da validação da idade

        if voltar == "sair":
            continue  # Retorna ao menu principal

        # Inserindo o novo usuário no banco de dados
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO usuarios (nome, email, senha, idade) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nome, email, senha, idade))
            conexao.commit()
            cursor.close()
            print("Usuário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar usuário: {err}")

        while input("Pressione ENTER para continuar...") != "":
            pass

    elif opcao == '2':
        print("=" * 50)
        print(" " * 15 + "LOGIN")
        print("=" * 50)

        # Tentativa de login com verificação de credenciais
        usuario_logado = None
        while True:
            email_login = input("Digite seu e-mail: ").strip()
            senha_login = input("Digite sua senha: ").strip()

            # Verificando as credenciais de login no banco de dados
            try:
                cursor = conexao.cursor()
                sql = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
                cursor.execute(sql, (email_login, senha_login))
                usuario = cursor.fetchone()
                cursor.close()

                if usuario:
                    print("Login realizado com sucesso!")
                    usuario_logado = usuario
                    id_usuario = usuario[0]  # ID do usuário para futuras operações
                    break
                else:
                    print("Erro: E-mail ou senha incorretos.")
                    while True:
                        tentar_novamente = input(
                            "Pressione ENTER para tentar novamente ou digite 'sair' para voltar ao menu: ").strip().lower()
                        if tentar_novamente == "sair":
                            break
                        elif tentar_novamente == "":
                            break
                        else:
                            print("Entrada inválida. Digite 'sair' ou pressione apenas ENTER para tentar novamente.")
                    if tentar_novamente == "sair":
                        break
            except mysql.connector.Error as err:
                print(f"Erro ao realizar login: {err}")
                break

        if not usuario_logado:
            continue

        # Menu pós-login
        while True:
            print("=" * 50)
            print(" " * 15 + "MENU DO USUÁRIO")
            print("=" * 50)
            print("[1] Gerenciar Treinos")
            print("[2] Registrar Progresso")
            print("[3] Visualizar Histórico de Progresso")
            print("[4] Gerenciar Perfil")
            print("[5] Sair")
            print("=" * 50)

            opcao_pos_login = input("Digite a opção desejada: ").strip()

            if opcao_pos_login == '1':
                # Gerenciar Treinos
                while True:
                    print("=" * 50)
                    print(" " * 15 + "GERENCIAR TREINOS")
                    print("=" * 50)
                    print("[1] Criar Novo Treino")
                    print("[2] Listar Treinos Existentes")
                    print("[3] Editar Treino")
                    print("[4] Remover Treino")
                    print("[5] Voltar")
                    print("=" * 50)

                    opcao_treino = input("Digite a opção desejada: ").strip()

                    if opcao_treino == '1':
                        # Criar Novo Treino
                        print("=" * 50)
                        print(" " * 15 + "CRIAR NOVO TREINO")
                        print("=" * 50)

                        # Solicitar o nome do treino
                        nome_treino = input("Digite o nome do treino: ").strip()
                        if not nome_treino:
                            print("O nome do treino não pode ser vazio.")
                            continue

                        # Escolher uma periodização
                        while True:
                            print("Escolha a periodização para o treino:")
                            try:
                                cursor = conexao.cursor()
                                cursor.execute("SELECT idperiodizacao, nome FROM Periodizacao")
                                periodizacoes = cursor.fetchall()
                                cursor.close()

                                if not periodizacoes:
                                    print("Nenhuma periodização encontrada. Cadastre uma periodização primeiro.")
                                    break

                                for idx, periodizacao in enumerate(periodizacoes):
                                    print(f"[{idx + 1}] {periodizacao[1]}")
                                escolha_periodizacao = input("Digite o número da periodização desejada: ").strip()

                                if not escolha_periodizacao.isdigit() or not (
                                        1 <= int(escolha_periodizacao) <= len(periodizacoes)):
                                    print("Escolha inválida. Tente novamente.")
                                    continue

                                id_periodizacao = periodizacoes[int(escolha_periodizacao) - 1][0]
                                break  # Sai do loop de escolha de periodização

                            except mysql.connector.Error as err:
                                print(f"Erro ao obter periodizações: {err}")
                                continue

                        # Inserir o treino na tabela Treinos
                        try:
                            cursor = conexao.cursor()
                            sql = "INSERT INTO Treinos (id_usuario, id_periodizacao, nome) VALUES (%s, %s, %s)"
                            cursor.execute(sql, (id_usuario, id_periodizacao, nome_treino))
                            conexao.commit()
                            id_treino = cursor.lastrowid
                            cursor.close()
                            print("Treino criado com sucesso!")
                        except mysql.connector.Error as err:
                            print(f"Erro ao criar treino: {err}")
                            continue

                        # Adicionar exercícios ao treino
                        while True:
                            print("=" * 50)
                            print(" " * 15 + "ADICIONAR EXERCÍCIO")
                            print("=" * 50)

                            # Escolher um exercício da tabela Exercicios, exibindo por grupo muscular
                            try:
                                cursor = conexao.cursor()
                                cursor.execute(
                                    "SELECT grupo_muscular, idexercicio, nome FROM Exercicios ORDER BY grupo_muscular")
                                exercicios = cursor.fetchall()
                                cursor.close()

                                if not exercicios:
                                    print("Nenhum exercício encontrado. Cadastre um exercício primeiro.")
                                    break

                                grupo_atual = None
                                for idx, exercicio in enumerate(exercicios):
                                    grupo_muscular = exercicio[0]
                                    if grupo_muscular != grupo_atual:
                                        grupo_atual = grupo_muscular
                                        print(f"\n[{grupo_muscular}]")
                                    print(f"  [{idx + 1}] {exercicio[2]}")

                                escolha_exercicio = input("\nDigite o número do exercício desejado: ").strip()

                                if not escolha_exercicio.isdigit() or not (
                                        1 <= int(escolha_exercicio) <= len(exercicios)):
                                    print("Escolha inválida.")
                                    continue

                                id_exercicio = exercicios[int(escolha_exercicio) - 1][1]

                            except mysql.connector.Error as err:
                                print(f"Erro ao obter exercícios: {err}")
                                continue

                            # Inserir múltiplas séries com a mesma configuração
                            while True:
                                try:
                                    # Validar número de séries
                                    while True:
                                        try:
                                            num_series = int(input("Digite o número de séries: ").strip())
                                            if num_series <= 0:
                                                print("Entrada inválida: O número de séries deve ser positivo.")
                                            else:
                                                break
                                        except ValueError:
                                            print(
                                                "Entrada inválida: digite um número positivo..")

                                    # Validar número de repetições
                                    while True:
                                        try:
                                            repeticoes = int(input("Digite o número de repetições por série: ").strip())
                                            if repeticoes <= 0:
                                                print("Entrada inválida: O número de repetições deve ser positivo.")
                                            else:
                                                break
                                        except ValueError:
                                            print(
                                                "Entrada inválida. digite um número positivo para as repetições.")

                                    # Validar carga
                                    while True:
                                        try:
                                            carga = float(input("Digite a carga (em kg) para cada série: ").strip())
                                            if carga <= 0:
                                                print("Entrada inválida: A carga deve ter um valor positivo.")
                                            else:
                                                break
                                        except ValueError:
                                            print("Entrada inválida. Digite um número  positivo para a carga.")

                                    cursor = conexao.cursor()
                                    valores = [(id_treino, id_exercicio, 1, repeticoes, carga) for _ in
                                               range(num_series)]
                                    sql = "INSERT INTO TreinoDetalhes (id_treino, id_exercicio, series, repeticoes, carga) VALUES (%s, %s, %s, %s, %s)"
                                    cursor.executemany(sql, valores)
                                    conexao.commit()
                                    cursor.close()
                                    print(f"{num_series} séries adicionadas com sucesso!")

                                except mysql.connector.Error as err:
                                    print(f"Erro ao adicionar séries: {err}")
                                    break

                                while True:
                                    adicionar_mais_exercicios = input(
                                        "Deseja adicionar outro exercício? (s/n): ").strip().lower()
                                    if adicionar_mais_exercicios in ['s', 'n']:
                                        break
                                    else:
                                        print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

                                if adicionar_mais_exercicios == 's':
                                    break
                                else:
                                    print("Exercícios cadastrados com sucesso!")
                                    break

                            if adicionar_mais_exercicios == 'n':
                                break  # Sai do loop principal de adição de exercícios

                    elif opcao_treino == '2':
                        print("=" * 50)
                        print(" " * 15 + "LISTA DE TREINOS")
                        print("=" * 50)
                        try:
                            cursor = conexao.cursor()
                            sql = """
                                SELECT T.idtreino, T.nome, P.nome AS periodizacao
                                FROM Treinos T
                                LEFT JOIN Periodizacao P ON T.id_periodizacao = P.idperiodizacao
                                WHERE T.id_usuario = %s
                            """
                            cursor.execute(sql, (id_usuario,))
                            treinos = cursor.fetchall()
                            cursor.close()

                            if not treinos:
                                print("Nenhum treino encontrado.")
                                continue

                            for treino in treinos:
                                print(f"ID: {treino[0]}, Nome: {treino[1]}, Periodização: {treino[2]}")

                        except mysql.connector.Error as err:
                            print(f"Erro ao listar treinos: {err}")

                    elif opcao_treino == '3':

                        # Exibir lista de treinos para que o usuário possa selecionar o ID desejado
                        print("=" * 50)
                        print(" " * 15 + "EDITAR TREINO")
                        print("=" * 50)
                        print("Treinos disponíveis:")

                        # Listar os treinos do usuário logado
                        try:
                            cursor = conexao.cursor()
                            sql = "SELECT idtreino, nome FROM Treinos WHERE id_usuario = %s"
                            cursor.execute(sql, (id_usuario,))
                            treinos = cursor.fetchall()
                            cursor.close()

                            if not treinos:
                                print("Nenhum treino encontrado para editar.")
                                while input("Pressione ENTER para voltar ao menu...") != "":
                                    pass
                                continue

                            for treino in treinos:
                                print(f"ID: {treino[0]}, Nome: {treino[1]}")

                        except mysql.connector.Error as err:
                            print(f"Erro ao listar treinos: {err}")
                            while input("Pressione ENTER para voltar ao menu...") != "":
                                pass
                            continue

                        # Escolher o treino para edição
                        while True:
                            id_treino_editar = input("Digite o ID do treino que deseja editar: ").strip()
                            if not id_treino_editar.isdigit():
                                print("Entrada inválida. Digite um número inteiro positivo para o ID do treino.")
                                continue
                            id_treino_editar = int(id_treino_editar)
                            if not any(t[0] == id_treino_editar for t in treinos):
                                print("ID do treino não encontrado. Tente novamente.")
                                continue
                            break

                        # Editar o nome do treino
                        novo_nome_treino = input(
                            "Digite o novo nome para o treino (ou pressione ENTER para manter): ").strip()
                        if novo_nome_treino:
                            try:
                                cursor = conexao.cursor()
                                sql = "UPDATE Treinos SET nome = %s WHERE idtreino = %s"
                                cursor.execute(sql, (novo_nome_treino, id_treino_editar))
                                conexao.commit()
                                cursor.close()
                                print("Nome do treino atualizado com sucesso!")
                            except mysql.connector.Error as err:
                                print(f"Erro ao atualizar o nome do treino: {err}")
                                while input("Pressione ENTER para voltar ao menu...") != "":
                                    pass
                                continue

                        # Editar os exercícios do treino
                        print("\n--- Editar Exercícios do Treino ---")

                        # Listar séries associadas ao treino
                        try:
                            cursor = conexao.cursor()
                            sql = """
                                        SELECT TD.idtreinodetalhe, E.nome, TD.series, TD.repeticoes, TD.carga
                                        FROM TreinoDetalhes TD
                                        JOIN Exercicios E ON TD.id_exercicio = E.idexercicio
                                        WHERE TD.id_treino = %s
                                    """
                            cursor.execute(sql, (id_treino_editar,))
                            series = cursor.fetchall()
                            cursor.close()

                            if not series:
                                print("Nenhuma série encontrada para este treino.")
                                while input("Pressione ENTER para voltar ao menu...") != "":
                                    pass
                                continue

                            for serie in series:
                                print(
                                    f"ID Série: {serie[0]}, Exercício: {serie[1]}, Séries: {serie[2]}, Repetições: {serie[3]}, Carga: {serie[4]} kg")

                        except mysql.connector.Error as err:
                            print(f"Erro ao listar exercícios do treino: {err}")
                            while input("Pressione ENTER para voltar ao menu...") != "":
                                pass
                            continue

                        # Loop para edição das séries
                        while True:
                            escolha = input(
                                "\nDigite o ID da série que deseja editar ou 'nova' para adicionar uma nova série: ").strip().lower()

                            if escolha == 'nova':
                                print("\n--- Adicionar Nova Série ---")
                                # Exibir lista de exercícios disponíveis
                                try:
                                    cursor = conexao.cursor()
                                    cursor.execute("SELECT idexercicio, nome FROM Exercicios")
                                    exercicios = cursor.fetchall()
                                    cursor.close()

                                    if not exercicios:
                                        print("Nenhum exercício encontrado para adicionar. Cadastre exercícios antes.")
                                        while input("Pressione ENTER para voltar ao menu...") != "":
                                            pass
                                        break

                                    for exercicio in exercicios:
                                        print(f"ID: {exercicio[0]}, Nome: {exercicio[1]}")

                                    # Seleção de exercício
                                    while True:
                                        id_exercicio = input("Digite o ID do exercício desejado: ").strip()
                                        if id_exercicio.isdigit() and any(
                                                ex[0] == int(id_exercicio) for ex in exercicios):
                                            id_exercicio = int(id_exercicio)
                                            break
                                        print("ID de exercício inválido. Digite novamente.")

                                    # Inserir nova série com validações de entradas numéricas
                                    while True:
                                        try:
                                            repeticoes = int(input("Digite o número de repetições por série: ").strip())
                                            if repeticoes > 0:
                                                break
                                            else:
                                                print("O número de repetições deve ser positivo.")
                                        except ValueError:
                                            print("Entrada inválida. Digite um número inteiro.")

                                    while True:
                                        try:
                                            carga = float(input("Digite a carga (em kg) para cada série: ").strip())
                                            if carga > 0:
                                                break
                                            else:
                                                print("A carga deve ser um número positivo.")
                                        except ValueError:
                                            print("Entrada inválida. Digite um número decimal.")

                                    # Inserir nova série no banco
                                    try:
                                        cursor = conexao.cursor()
                                        sql = "INSERT INTO TreinoDetalhes (id_treino, id_exercicio, series, repeticoes, carga) VALUES (%s, %s, 1, %s, %s)"
                                        cursor.execute(sql, (id_treino_editar, id_exercicio, repeticoes, carga))
                                        conexao.commit()
                                        cursor.close()
                                        print("Nova série adicionada com sucesso!")
                                    except mysql.connector.Error as err:
                                        print(f"Erro ao adicionar nova série: {err}")
                                        break

                                except mysql.connector.Error as err:
                                    print(f"Erro ao listar exercícios: {err}")
                                    while input("Pressione ENTER para voltar ao menu...") != "":
                                        pass
                                    break

                            elif escolha.isdigit() and int(escolha) in [serie[0] for serie in series]:
                                id_serie = int(escolha)
                                print("\n--- Editar Série Existente ---")
                                # Encontrar a série a ser editada
                                serie_atual = next(serie for serie in series if serie[0] == id_serie)

                                # Edição de campos da série
                                while True:
                                    try:
                                        repeticoes = int(input(f"Repetições (atual {serie_atual[3]}): ").strip())
                                        if repeticoes > 0:
                                            break
                                        else:
                                            print("O número de repetições deve ser positivo.")
                                    except ValueError:
                                        print("Entrada inválida. Digite um número inteiro.")

                                while True:
                                    try:
                                        carga = float(input(f"Carga (atual {serie_atual[4]} kg): ").strip())
                                        if carga > 0:
                                            break
                                        else:
                                            print("A carga deve ser um número positivo.")
                                    except ValueError:
                                        print("Entrada inválida. Digite um número decimal.")

                                # Atualizar a série no banco de dados
                                try:
                                    cursor = conexao.cursor()
                                    sql = "UPDATE TreinoDetalhes SET repeticoes = %s, carga = %s WHERE idtreinodetalhe = %s"
                                    cursor.execute(sql, (repeticoes, carga, id_serie))
                                    conexao.commit()
                                    cursor.close()
                                    print("Série atualizada com sucesso!")
                                except mysql.connector.Error as err:
                                    print(f"Erro ao atualizar a série: {err}")
                                    break
                            else:
                                print("Opção inválida. Tente novamente.")
                                continue

                            # Perguntar se o usuário deseja continuar editando
                            while True:
                                continuar = input("Deseja continuar editando? (s/n): ").strip().lower()
                                if continuar in ['s', 'n']:
                                    break
                                print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

                            if continuar == 'n':
                                break


                    elif opcao_treino == '4':
                        print("=" * 50)
                        print(" " * 15 + "REMOVER TREINO")
                        print("=" * 50)
                        print("Treinos disponíveis:")

                        # Listar os treinos do usuário logado
                        try:
                            cursor = conexao.cursor()
                            sql = "SELECT idtreino, nome FROM Treinos WHERE id_usuario = %s"
                            cursor.execute(sql, (id_usuario,))
                            treinos = cursor.fetchall()
                            cursor.close()

                            if not treinos:
                                print("Nenhum treino encontrado para remover.")
                                continue  # Volta ao menu principal automaticamente se não há treinos

                            for treino in treinos:
                                print(f"ID: {treino[0]}, Nome: {treino[1]}")
                            print(
                                "Digite o ID do treino que deseja remover ou 'voltar' para retornar ao menu anterior.")

                        except mysql.connector.Error as err:
                            print(f"Erro ao listar treinos: {err}")
                            continue  # Volta ao menu principal automaticamente em caso de erro

                        # Solicitar ID do treino ou opção de voltar
                        while True:
                            id_treino_remover = input("Digite o ID do treino ou 'voltar': ").strip().lower()

                            # Verificar se o usuário optou por voltar
                            if id_treino_remover == 'voltar':
                                print("Operação de remoção cancelada. Retornando ao menu anterior.")
                                break  # Sai do loop e volta ao menu automaticamente

                            # Validar o ID digitado
                            if not id_treino_remover.isdigit():
                                print("Entrada inválida. Digite um número inteiro para o ID ou 'voltar' para retornar.")
                                continue

                            id_treino_remover = int(id_treino_remover)

                            # Verificar se o ID do treino existe na lista de treinos
                            if not any(t[0] == id_treino_remover for t in treinos):
                                print("ID do treino não encontrado. Tente novamente.")
                                continue

                            # Confirmar remoção
                            treino_nome = next(t[1] for t in treinos if t[0] == id_treino_remover)
                            while True:
                                confirmacao = input(
                                    f"Tem certeza que deseja remover o treino '{treino_nome}'? (s/n): ").strip().lower()

                                if confirmacao == 's':
                                    # Remover o treino e suas séries
                                    try:
                                        cursor = conexao.cursor()
                                        cursor.execute("DELETE FROM TreinoDetalhes WHERE id_treino = %s",
                                                       (id_treino_remover,))
                                        cursor.execute("DELETE FROM Treinos WHERE idtreino = %s", (id_treino_remover,))
                                        conexao.commit()
                                        cursor.close()
                                        print(f"Treino '{treino_nome}' removido com sucesso!")
                                    except mysql.connector.Error as err:
                                        print(f"Erro ao remover o treino: {err}")
                                    break  # Sai do loop e volta ao menu automaticamente
                                elif confirmacao == 'n':
                                    print("Operação de remoção cancelada.")
                                    break  # Sai do loop e volta ao menu automaticamente
                                else:
                                    print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

                            # Quebra o loop principal após a confirmação para retornar ao menu
                            if confirmacao in ['s', 'n']:
                                break

            elif opcao_pos_login == '2':
                print("Opção: Registrar Progresso")
                while input("Pressione ENTER para continuar...") != "":
                    pass

            elif opcao_pos_login == '3':
                print("Opção: Visualizar Histórico de Progresso")
                while input("Pressione ENTER para continuar...") != "":
                    pass

            elif opcao_pos_login == '4':
                print("Opção: Gerenciar Perfil")
                while input("Pressione ENTER para continuar...") != "":
                    pass

            elif opcao_pos_login == '5':
                print("Saindo do sistema de usuário...")
                break
            else:
                print("Opção inválida.")
                while input("Pressione ENTER para continuar...") != "":
                    pass

    elif opcao == '3':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
        while input("Pressione ENTER para continuar...") != "":
            pass

# Fechando a conexão com o banco de dados
conexao.close()


