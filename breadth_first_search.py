from constant import database_instance, nodes_query_sql, nodes_query_sql_parents, get_node
from utils import lists_have_same_elements


class BreadthFirstSearch:

    def __init__(self):
        self.tail = []
        self.extracted = []
        self.found = []

    def search(self, initial_node, final_nodes):
        try:
            database_instance.connect()
            current = initial_node
            rows = database_instance.execute_sql(nodes_query_sql, (current,))

            if rows is None or len(rows) == 0:
                raise Exception('El nodo ' + current + ' no existe...')

            self.tail.append(current)

            while len(self.tail) > 0:
                if self.final_nodes_are_found(final_nodes):
                    break

                self.add_found(current, final_nodes)

                self.add_extracted(current)

                self.tail.remove(current)

                self.add_to_tail(rows)

                current = self.tail[0]

                rows = database_instance.execute_sql(nodes_query_sql, (current,))

        except Exception as error:
            print(error)
        finally:
            database_instance.close()

    def final_nodes_are_found(self, final_nodes):
        if final_nodes is None:
            return False

        if isinstance(final_nodes, list):
            return lists_have_same_elements(self.found, final_nodes)

        return len(self.found) == 1 and self.found[0] == final_nodes

    def add_found(self, current_node, final_nodes):
        if final_nodes is None:
            return False

        if isinstance(final_nodes, list):
            if current_node in final_nodes and current_node not in self.found:
                self.found.append(current_node)
                return True

        if current_node == final_nodes and len(self.found) == 0:
            self.found.append(current_node)
            return True

        return False

    def add_to_tail(self, rows):
        for row in rows:
            if row is not None:
                row = get_node(row)
                if row not in self.extracted and row not in self.tail:
                    self.tail.append(row)

    def add_extracted(self, current_node):
        if current_node not in self.extracted:
            self.extracted.append(current_node)
            return True

        return False

