from utilities.constant import database_instance, nodes_query_sql, get_node_with_cost


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
                self.queue.remove(current)
                self.add_extracted(current)

                if current[0] == dest:
                    self.found = current
                    break

                successors = database_instance.execute_sql(nodes_query_sql, (current[0],))
                self.add_to_queue(successors, current[1])
                if len(self.queue) > 0:
                    current = self.queue[0]

        except Exception as error:
            print(error)
        finally:
            database_instance.close()

    def add_extracted(self, current_node):
        if current_node not in self.extracted:
            self.extracted.append(current_node)
            return True

        return False

    def add_to_queue(self, rows, total_cost):
        for row in rows:
            if row is not None:
                row = get_node_with_cost(row)
                if not self.node_has_shown(row):
                    node = list(row)
                    node[1] += total_cost
                    self.queue.append(tuple(node))
                else:
                    new_node = list(row)
                    new_node[1] += total_cost

                    existent_node = self.get_existent_node(row, self.queue)
                    if existent_node is None:
                        existent_node = self.get_existent_node(row, self.extracted)
                        if existent_node[1] > new_node[1]:
                            self.queue.append(tuple(new_node))
                            self.extracted.remove(existent_node)
                    else:
                        if existent_node[1] > new_node[1]:
                            idx = self.queue.index(existent_node)
                            self.queue[idx] = tuple(new_node)

        self.queue.sort(key=sort_key)

    def node_has_shown(self, node):
        for n in self.queue:
            if n[0] == node[0]:
                return True

        for n in self.extracted:
            if n[0] == node[0]:
                return True

        return False

    def get_existent_node(self, node, array):
        for n in array:
            if n[0] == node[0]:
                return n
        return None
