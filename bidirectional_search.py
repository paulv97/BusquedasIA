from constant import database_instance, nodes_query_sql, nodes_query_sql_parents, get_node
from utils import lists_have_same_elements


class BidirectionalSearch:

    def __init__(self):
        self.init_queue = []
        self.init_extracted = []
        self.goal_queue = []
        self.goal_extracted = []

    def search(self, src, dest):
        try:
            database_instance.connect()

            current_init = src
            rows_init = database_instance.execute_sql(nodes_query_sql, (current_init,))

            if rows_init is None or len(rows_init) == 0:
                raise Exception('El nodo ' + current_init + ' no existe...')

            self.init_queue.append(current_init)

            if dest is None:
                raise Exception('No hay nodo final para buscar')

            current_meta = None
            rows_meta = []
            current_meta = dest
            rows_meta = database_instance.execute_sql(nodes_query_sql_parents, (current_meta,))
            if rows_meta is None or len(rows_meta) == 0:
                raise Exception('El nodo ' + current_meta + ' no existe...')
            self.goal_queue.append(current_meta)

            while len(self.init_queue) > 0 and len(self.goal_queue) > 0:
                self.init_queue.remove(current_init)
                self.add_extracted(self.init_extracted, current_init)
                self.add_to_tail(self.init_queue, self.init_extracted, rows_init)
                if current_init in self.goal_queue:
                    break
                if len(self.init_queue) > 0:
                    current_init = self.init_queue[0]
                    rows_init = database_instance.execute_sql(nodes_query_sql, (current_init,))

                self.goal_queue.remove(current_meta)
                self.add_extracted(self.goal_extracted, current_meta)
                self.add_to_tail(self.goal_queue, self.goal_extracted, rows_meta)
                if current_meta in self.init_queue:
                    break
                if len(self.goal_queue) > 0:
                    current_meta = self.goal_queue[0]
                    rows_meta = database_instance.execute_sql(nodes_query_sql_parents, (current_meta,))
        except Exception as error:
            print(error)
        finally:
            database_instance.close()

    def add_to_tail(self, tail, extracted, rows):
        for row in rows:
            if row is not None:
                row = get_node(row)
                if row not in extracted and row not in tail:
                    tail.append(row)


    def add_extracted(self, extracted, current_node):
        if current_node not in extracted:
            extracted.append(current_node)
            return True

        return False
