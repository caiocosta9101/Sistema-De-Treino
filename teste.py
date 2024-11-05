import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'musculacao'
)


def exibir_linha():
    print('=' * 50)



def exbir_menu_principal():
    exibir_linha()
    print('sistema de treino')
    exibir_linha
    print('escolha uma opção: ')
    print(' [1] Cadastrar usuário')
    print(' [2] login')
    print(' [3] sair')
    exibir_linha

def obter_obter_numero_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor > 0:
                return valor
            else:
                print("erro: O valor deve ser um número positivo.")
        except ValueError:
            print('erro: por favor digite um número válido')

def tentar_novamente_ou_sair(mensagem="pressione 'enter' pra tentar novamente ou digite 'sair' para voltar ao menu."):
    resposta = input(mensagem).strip().lower()
    if resposta == 'sair':
        return False
    return True
