from database import conectar
import os

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

    if restaurantes != []:
        for restaurante in restaurantes:
            id = restaurante[0]
            nome = restaurante[1]
            categoria = restaurante[2]
            ativo = bool(restaurante[3])
            status = "Ativo" if ativo else "Inativo"
            print(f"{id}  | {nome.ljust(20)} | {categoria.ljust(20)} | {status}")
    else:
        os.system('cls')
        print("Nenhum restaurante cadastrado.")
        return "vazio"

def alterar_status_restaurante(id_restaurante):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT ativo FROM restaurantes WHERE id = ?", (id_restaurante,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return None

    novo_status = 0 if resultado[0] else 1

    cursor.execute("""
        UPDATE restaurantes
        SET ativo = ?
        WHERE id = ?
    """, (novo_status, id_restaurante))

    conexao.commit()
    conexao.close()

    return bool(novo_status)

def editar_restaurante_nome(id_restaurante):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM restaurantes WHERE id = ?", (id_restaurante,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return None

    edit_nome = input("Digite o novo nome do restaurante: ")

    cursor.execute("""
        UPDATE restaurantes
        SET nome = ?
        WHERE id = ?
    """, (edit_nome, id_restaurante))

    conexao.commit()
    conexao.close()

    return edit_nome

def editar_restaurante_categoria(id_restaurante):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT categoria FROM restaurantes WHERE id = ?", (id_restaurante,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return None

    edit_categoria = input("Digite a nova categoria do restaurante: ")

    cursor.execute("""
        UPDATE restaurantes
        SET categoria = ?
        WHERE id = ?
    """, (edit_categoria, id_restaurante))

    conexao.commit()
    conexao.close()

    return edit_categoria

def eliminar_restaurante(id_restaurante):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM restaurantes WHERE id = ?", (id_restaurante,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexao.close()
        return None

    cursor.execute("DELETE FROM restaurantes WHERE id = ?", (id_restaurante,))
    conexao.commit()
    conexao.close()

    return resultado[0]
