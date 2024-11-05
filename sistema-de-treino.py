import mysql.connector

# Configurando a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='',#coloque o seu user
    password='',#coloque sua senha
    database=''#coloque sua base de dados do mysql
)

# Função para exibir uma linha decorativa
def exibir_linha():
    print("=" * 50)

# Função para exibir o menu principal do sistema
def exibir_menu_principal():
    exibir_linha()
    print("Sistema de Gerenciamento de Treino")
    exibir_linha()
    print("Escolha uma opção: ")
    print(" [1] Cadastrar Usuário")
    print(" [2] Login")
    print(" [3] Sair")
    exibir_linha()

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

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    exibir_linha()
    print("Cadastro de Usuário")
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
    print("LOGIN")
    exibir_linha()
    
    while True:
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite sua senha: ").strip()

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
    print(" " * 15 + "MENU DO USUÁRIO")
    exibir_linha()
    print("[1] Gerenciar Treinos")
    print("[2] Registrar Progresso")
    print("[3] Visualizar Histórico de Progresso")
    print("[4] Gerenciar Perfil")
    print("[5] Sair")
    exibir_linha()

# Função para gerenciar treinos (submenu)
def exibir_menu_gerenciar_treinos():
    exibir_linha()
    print(" " * 15 + "GERENCIAR TREINOS")
    exibir_linha()
    print("[1] Criar Novo Treino")
    print("[2] Listar Treinos Existentes")
    print("[3] Editar Treino")
    print("[4] Remover Treino")
    print("[5] Voltar")
    exibir_linha()

# Função para o fluxo de gerenciamento de treinos
def gerenciar_treinos():
    while True:
        exibir_menu_gerenciar_treinos()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            print("Opção: Criar Novo Treino")
            # Lógica para criar um novo treino
        elif opcao == '2':
            print("Opção: Listar Treinos Existentes")
            # Lógica para listar treinos existentes
        elif opcao == '3':
            print("Opção: Editar Treino")
            # Lógica para editar um treino
        elif opcao == '4':
            print("Opção: Remover Treino")
            # Lógica para remover um treino
        elif opcao == '5':
            print("Voltando ao menu do usuário...")
            break  # Retorna ao menu do usuário logado
        else:
            print("=" * 50)
            print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
            print("=" * 50)
            pausar_para_continuar()

# Função para o menu do usuário logado
def menu_usuario_logado(usuario):
    while True:
        exibir_menu_usuario()
        opcao = input("Digite a opção desejada: ").strip()

        if opcao == '1':
            gerenciar_treinos()  # Chama o submenu de gerenciamento de treinos
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
            print("=" * 50)
            print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
            print("=" * 50)
            pausar_para_continuar()

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
        print("=" * 50)
        print("ERRO: Opção inválida! Por favor, escolha uma opção válida.")
        print("=" * 50)
        pausar_para_continuar()

# Fechando a conexão com o banco de dados
conexao.close()




