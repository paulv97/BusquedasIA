import psycopg2


class Database:

    def __init__(self, **database_args):
        self.host = database_args["host"]
        self.database = database_args["database"]
        self.user = database_args["user"]
        self.password = database_args["password"]
        self.port = database_args["port"]
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )

    def execute_sql(self, sql, *params):
        if self.conn is None:
            raise Exception('Database connection should be established first...')
        try:
            cur = self.conn.cursor()
            cur.execute(sql, params)
            rows = cur.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print('Database error....' + error)
            raise Exception('Algo salio mal al ejecutar la consulta...')

    def execute_transaction(self, sql, params):
        if self.conn is None:
            raise Exception('Database connection should be established first...')
        try:
            cur = self.conn.cursor()
            if isinstance(params, list):
                for row in params:
                    cur.execute(sql, row)
            else:
                cur.execute(sql, params)

            self.conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print('Database error....' + error)
            raise Exception('Algo salio mal al ejecutar la transaccion...')

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
