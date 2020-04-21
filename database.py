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
        self.conn = sqlite3.connect(self.db_name)
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

    def validate_table_exist(self, table_name):
        return table_name in self.tables

    def get_all(self, table_name):
        if self.validate_table_exist:
            columns_list = [value for key, value in self.tables[table_name].items()]
            columns = ','.join(columns_list)
            sql = f'SELECT {columns} FROM {table_name}'
            rows = conn.execute(sql)
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
            rows = conn.execute(sql)
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
            sql = '''
                INSERT INTO
                f'{table_name}'
                .
            '''


