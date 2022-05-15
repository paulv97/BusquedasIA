from database import Database

database_instance = Database(
    host="localhost",
    database="ia",
    user="postgres",
    password="12345",
    port=5432
)

nodes_query_sql = """SELECT id_nodo_conecta, peso 
            FROM nodos WHERE upper(id_nodo)=%s
            order by id_nodo_conecta;"""

nodes_query_sql_parents = """SELECT id_nodo, peso 
            FROM nodos WHERE upper(id_nodo_conecta)=%s
            order by id_nodo;"""


def get_node(row):
    return row[0].upper().replace(" ", "")


def get_node_with_cost(row):
    node = row[0].upper().replace(" ", "")
    cost = row[1]
    return node, cost

