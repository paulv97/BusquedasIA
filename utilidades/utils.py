import psycopg2

from utilidades.constant import database_instance


def cargar_archivo(filename='nodes.csv'):
    nodes_file = open(filename, 'r')
    nodes_list = nodes_file.readlines()
    nodes_file.close()
    return nodes_list


def llenar_tabla(lista_nodos):
    try:
        database_instance.connect()

        delete_sql = "DELETE FROM nodos;"
        insert_sql = """INSERT INTO nodos(id_nodo, id_nodo_conecta, peso, fev)
                VALUES(%s, %s, %s, %s) RETURNING id_nodo;"""

        database_instance.execute_transaction(delete_sql, None)

        for data in lista_nodos:
            obj = data.split(',')
            id_nodo = obj[0]
            id_nodo_conecta = obj[1]
            peso = obj[2]
            fev = obj[3].replace('\n', '')
            database_instance.execute_transaction(insert_sql, (id_nodo, id_nodo_conecta, peso, fev))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        database_instance.close()


def lists_have_same_elements(list_a, list_b):
    la = list_a.copy()
    lb = list_b.copy()
    la.sort()
    lb.sort()
    return la == lb