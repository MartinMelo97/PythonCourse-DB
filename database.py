import sqlite3

class Database:
    db_name = 'papitas.db'
    tables = {
        'papita': {
            'name': 'name',
            'price': 'price',
            'description': 'desc',
            'color': 'color'
        }
    }

    def __init__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.conn = self.connection.cursor()
        print('Database connection is open')
        self.create_papita_table()

    def create_papita_table(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS papita (
                name VARCHAR NOT NULL,
                price DOUBLE NOT NULL,
                desc TEXT NULL,
                color VARCHAR NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        '''
        self.conn.execute(sql)
        print("Table created")

    def validate_table_exist(self, table_name):
        return table_name in self.tables

    def get_all(self, table_name):
        if self.validate_table_exist:
            columns_list = [value for key, value in self.tables[table_name].items()]
            columns = ','.join(columns_list)
            sql = f'SELECT {columns} FROM {table_name}'
            rows = self.conn.execute(sql)
            result = {
                'error': False,
                'rows': rows
            }
            return result
        else:
            result = {
                'error': True,
                'message': 'Table does not exist in column'
            }

    def get_one(self, table_name, id):
        if self.validate_table_exist:
            columns_list = [value for key, value in self.tables[table_name].items()]
            columns = ','.join(columns_list)
            id_column_name = self.tables[table_name]['id']
            sql = f'SELECT {columns} FROM {table_name} WHERE {id_column_name} = id'
            rows = self.conn.execute(sql)
            result = {
                'error': False,
                'rows': rows
            }
            return result
        else:
            result = {
                'error': True,
                'message': 'Table does not exist in column'
            }

    def create(self, table_name, data):
        if self.validate_table_exist:
            columns_list = [value for key, value in self.tables[table_name].items()]
            columns = ','.join(columns_list)
            sql = f'INSERT INTO {table_name} ({columns}) VALUES ({",".join(["?" for i in range(len(columns_list))])})'
            new_row = self.conn.execute(sql, data)
            self.connection.commit()
            return self.conn.lastrowid



