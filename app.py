import os
from database import criar_tabelas, conectar

"""restaurantes = [
    {"nome": "Restaurante A", "categoria": "Italiana", "ativo": False}, 
    {"nome": "Restaurante B", "categoria": "Brasileira", "ativo": True}, 
    {"nome": "Restaurante C", "categoria": "Japonesa", "ativo": False}
]"""

def exibir_nome_app():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_menu_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alterar status do restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system('cls')
    print("Encerrando o programa...\n")
    return True

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return 4
            case _:
                return False
    except ValueError:
        return False

def cadastrar_restaurante():
    nome = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome}: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO restaurantes (nome, categoria, ativo)
        VALUES (?, ?, ?)
    """, (nome, categoria, 0))

    conexao.commit()
    conexao.close()

    return nome

def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM restaurantes")
    restaurantes = cursor.fetchall()
    conexao.close()

    for restaurante in restaurantes:
        nome = restaurante[1]
        categoria = restaurante[2]
        ativo = bool(restaurante[3])
        status = "Ativo" if ativo else "Inativo"
        print(f"- {nome.ljust(20)} | {categoria.ljust(20)} | {status}")

def voltar_menu():
    input("\nPressione Enter para continuar...")

def exibir_subtitulo(txt):
    os.system('cls')
    print(f"\n--- {txt} ---\n")

def alterar_status_restaurante(nome_restaurante):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT ativo FROM restaurantes WHERE nome = ?
    """, (nome_restaurante,))

    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return None

    novo_status = 0 if resultado[0] else 1

    cursor.execute("""
        UPDATE restaurantes
        SET ativo = ?
        WHERE nome = ?
    """, (novo_status, nome_restaurante))

    conexao.commit()
    conexao.close()

    return bool(novo_status)


def main():
        criar_tabelas()
        while True:
            os.system('cls')
            sair = False
            exibir_nome_app()
            exibir_menu_opcoes()
            while True:
                opc = escolher_opcao()
                match opc:
                    case 1:
                        exibir_subtitulo("Cadastro de novos restaurantes")
                        restaurante = cadastrar_restaurante()
                        print(f"\n O restaurante {restaurante} foi cadastrado com sucesso!")
                        voltar_menu()
                        break
                    case 2:
                        exibir_subtitulo("Lista de restaurantes cadastrados")
                        print("Nome do restaurante".ljust(22) + " | Categoria".ljust(23) + " | Status")
                        listar_restaurantes()
                        voltar_menu()
                        break
                    case 3:
                        exibir_subtitulo("Ativar restaurante")
                        nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")
                        status = alterar_status_restaurante(nome_restaurante)
                        if status is not None:
                            print(f"O restaurante {nome_restaurante} foi {'ativado' if status else 'desativado'} com sucesso!")
                            voltar_menu()
                            break
                        else:
                            print("Restaurante não encontrado.")
                            voltar_menu()
                            break
                    case 4:
                        sair = finalizar_app()
                        break
                    case False:
                        print('Opção inválida!')
                        continue

            if sair:
                break        
            else:
                continue
    
    

if __name__ == "__main__":
    main()