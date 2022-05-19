from utilidades.constant import database_instance, nodes_query_sql, get_node_with_cost


def sort_key(element):
    return element[1]


class UniformCostSearch:

    def __init__(self):
        self.queue = []
        self.extracted = []
        self.found = None

    def search(self, src, dest):
        try:
            database_instance.connect()
            current = (src, 0)
            rows = database_instance.execute_sql(nodes_query_sql, (current[0],))

            if rows is None or len(rows) == 0:
                raise Exception('El nodo ' + current[0] + ' no existe...')

            self.queue.append(current)

            while len(self.queue) > 0:
                if self.final_node_is_found(dest):
                    break

                self.add_found(current, dest)

                if current in self.queue:
                    self.queue.remove(current)
                    self.add_extracted(current)

                self.add_to_queue(rows)

                back_cost = current[1]
                current = self.queue[0]
                current_list = list(current)
                current_list[1] += back_cost
                current = tuple(current_list)

                rows = database_instance.execute_sql(nodes_query_sql, (current[0],))

        except Exception as error:
            print(error)
        finally:
            database_instance.close()

    def final_node_is_found(self, final_node):
        if final_node is None:
            return False

        return self.found == final_node

    def add_found(self, current_node, final_node):
        if final_node is None:
            return False

        if current_node[0] == final_node:
            self.found = current_node[0]
            return True

        return False

    def add_extracted(self, current_node):
        if current_node not in self.extracted:
            self.extracted.append(current_node)
            return True

        return False

    def add_to_queue(self, rows):
        for row in rows:
            if row is not None:
                row = get_node_with_cost(row)
                if row not in self.extracted and row not in self.queue:
                    self.queue.append(row)

        self.queue.sort(key=sort_key)
