from database import criar_tabelas
from ui import *
from services import *

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:
            case 1: return 1
            case 2: return 2
            case 3: return 3
            case 4: return 4
            case 5: return 5
            case 6: return 6
            case _: return False
    except ValueError:
        return False

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
                    print("ID " + "| Nome do restaurante".ljust(22) + " | Categoria".ljust(23) + " | Status")
                    listar_restaurantes()
                    voltar_menu()
                    break
                case 3:
                    exibir_subtitulo("Ativar restaurante")
                    print("ID " + "| Nome do restaurante".ljust(22) + " | Categoria".ljust(23) + " | Status")
                    vazio = listar_restaurantes()
                    if vazio == "vazio":
                        voltar_menu()
                        break
                    try:
                        id_restaurante = int(input("\nDigite o ID do restaurante a ser ativado/desativado: "))
                        status = alterar_status_restaurante(id_restaurante)
                        if status is not None:
                            print(f"O restaurante foi {'ativado' if status else 'desativado'} com sucesso!")
                        else:
                            print("Restaurante não encontrado.")
                        voltar_menu()
                        break
                    except ValueError:
                        print("ID inválido.")
                        voltar_menu()
                        break
                case 4:
                    exibir_subtitulo("Editar restaurante")
                    print("ID " + "| Nome do restaurante".ljust(22) + " | Categoria".ljust(23) + " | Status")
                    vazio = listar_restaurantes()
                    if vazio == "vazio":
                        voltar_menu()
                        break
                    try:
                        menu_edicao()
                        opcao_edicao = int(input("Escolha uma opção: "))
                        match opcao_edicao:
                            case 1:
                                id_restaurante = int(input("\nDigite o ID do restaurante a ser editado: "))
                                novo_nome = editar_restaurante_nome(id_restaurante)
                                if novo_nome:
                                    print("Restaurante editado com sucesso!")
                                else:
                                    print("Restaurante não encontrado.")
                                voltar_menu()
                                break
                            case 2:
                                id_restaurante = int(input("\nDigite o ID do restaurante a ser editado: "))
                                nova_categoria = editar_restaurante_categoria(id_restaurante)
                                if nova_categoria:
                                    print("Restaurante editado com sucesso!")
                                else:
                                    print("Restaurante não encontrado.")
                                voltar_menu()
                                break
                            case 3:
                                break
                    except ValueError:
                        print("ID inválido.")
                        voltar_menu()
                        break
                case 5:
                    exibir_subtitulo("Excluir restaurante")
                    print("ID " + "| Nome do restaurante".ljust(22) + " | Categoria".ljust(23) + " | Status")
                    vazio = listar_restaurantes()
                    if vazio == "vazio":
                        voltar_menu()
                        break
                    try:
                        id_restaurante = int(input("\nDigite o ID do restaurante a ser excluído: "))
                        eliminado = eliminar_restaurante(id_restaurante)
                        if eliminado:
                            print(f"{eliminado} foi excluído com sucesso!")
                        else:
                            print("Restaurante não encontrado.")
                        voltar_menu()
                        break
                    except ValueError:
                        print("ID inválido.")
                        voltar_menu()
                        break
                case 6:
                    sair = finalizar_app()
                    break
                case False:
                    print("Opção inválida!")
                    continue
        if sair:
            break

if __name__ == "__main__":
    main()