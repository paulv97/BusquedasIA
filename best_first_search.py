from constant import database_instance, nodes_fev_query_sql, get_node


class BestFirstSearch:

    def __init__(self):
        self.extracted = []
        self.found = None

    def search(self, src, dest):
        try:
            database_instance.connect()
            current = src

            self.extracted.append(current)
            if current == dest:
                self.add_found(current, dest)
                return

            rows = database_instance.execute_sql(nodes_fev_query_sql, (current,))

            if rows is None or len(rows) == 0:
                raise Exception('El nodo ' + current + ' no existe...')

            while len(rows) > 0:
                row = get_node(rows[0])
                while row in self.extracted:
                    rows.pop(0)
                    if len(rows) == 0:
                        row = None
                        break
                    row = get_node(rows[0])

                if row is None:
                    return

                current = row

                if current not in self.extracted:
                    self.extracted.append(current)

                if current == dest:
                    self.add_found(current, dest)
                    return

                rows = database_instance.execute_sql(nodes_fev_query_sql, (current,))

        except Exception as error:
            print(error)
        finally:
            database_instance.close()

    def add_found(self, current_node, final_node):
        if final_node is None:
            return False

        if current_node == final_node:
            self.found = current_node
            return True

        return False

