from database import Database

def validate_user_selection(selection):
    return isinstance(selection, int) and selection > 0 and selection < 4

def create(db):
    columns = db.tables['papita']
    data = [input(f'{column}: ') for column in columns]
    new_data = db.create('papita', data)
    print("Papita creada con el ID:", new_data)

def handle_user_selection(selection, db):
    if selection == 1:
        print('GetAll')
    elif selection == 2:
        print('Get One')
    else:
        create(db)

def main():
    db = Database()
    print('CRUD de papitas')
    print('1.Ver papitas registradas')
    print('2. Buscar papita por ID')
    print('3. Agregar papita')
    selection = int(input('¿Qué opción eliges?: '))
    if validate_user_selection(selection):
        handle_user_selection(selection, db)
    else:
        print("Selección inválida")

main()