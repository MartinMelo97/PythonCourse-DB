import sqlite3

# Create file for SQLite Database
# If file doesn't exist, it's created automatically
# Also, create database with the name (test)
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

# SQL Query to create new table
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS user (
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        phone_number VARCHAR(15),
        date_birth DATETIME,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
'''

# Creating new table
conn.execute(create_table_sql)
print("Table created succesfully")

# Inserting data

insert_sql = '''
    INSERT INTO
        user (first_name, last_name, email, phone_number)
    VALUES
        ('Martin', 'Melo', 'martin.melo.dev.97@gmail.com', '7721238271')
'''

insert_sql_v2 = '''
    INSERT INTO
        user (first_name, last_name, email, phone_number, date_birth)
    VALUES
        ('John', 'Lennon', 'john@beatles.', '1231231231', '1940-10-09')
'''

# conn.execute(insert_sql)
# conn.execute(insert_sql_v2)

# Commit insert all the data into the queries
# conn.commit()

# Getting data
select_all_sql = 'SELECT rowid, first_name, last_name, email, phone_number, date_birth, timestamp FROM user'
cursor = conn.execute(select_all_sql)
for row in cursor:
    print('\n')
    print(f'ID: {row[0]}')
    print(f'Nombre: {row[1]}')
    print(f'Apellidos: {row[2]}')
    print(f'Email: {row[3]}')
    print(f'Teléfono: {row[4]}')
    print(f'Fecha de nacimiento: {row[5]}') if row[5] else print('Fecha de nacimiento no especificada')
    print(f'Última actualización: {row[6]}')
    print('\n')

# Updating data
update_sql = '''
    UPDATE user SET first_name = 'Ringo' WHERE rowid = 1
'''

# conn.execute(update_sql)
# conn.commit()

# print('Rows updated: ', conn.total_changes)

# Deleting data
delete_sql = '''
    DELETE FROM user WHERE rowid = 2
'''
conn. execute(delete_sql)
conn.commit()

select_all_sql = 'SELECT rowid, first_name, last_name, email, phone_number, date_birth, timestamp FROM user'
cursor = conn.execute(select_all_sql)
for row in cursor:
    print('\n')
    print(f'ID: {row[0]}')
    print(f'Nombre: {row[1]}')
    print(f'Apellidos: {row[2]}')
    print(f'Email: {row[3]}')
    print(f'Teléfono: {row[4]}')
    print(f'Fecha de nacimiento: {row[5]}') if row[5] else print('Fecha de nacimiento no especificada')
    print(f'Última actualización: {row[6]}')
    print('\n')

# Close DB connection
conn.close()
print("Database connection closed")