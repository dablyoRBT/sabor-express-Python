import os

restaurantes = ["Restaurante A", "Restaurante B", "Restaurante C"]

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
    print("3. Ativar restaurante")
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
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    return nome_do_restaurante

def listar_restaurantes():
    for restaurante in restaurantes:
        print(f"- {restaurante}")

def voltar_menu():
    input("\nPressione Enter para continuar...")

def exibir_subtitulo(txt):
    os.system('cls')
    print(f"\n--- {txt} ---\n")

def main():
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
                        listar_restaurantes()
                        voltar_menu()
                        break
                    case 3:
                        print('Ativar restaurante')
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