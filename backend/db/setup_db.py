# setup_db.py
import sqlite3

# Conectarse a la base de datos (se creará si no existe)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Crear la tabla 'items'
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
''')

# Insertar datos de ejemplo
items_to_insert = [
    ('Laptop', 'Un portátil de alto rendimiento.'),
    ('Mouse', 'Un mouse ergonómico inalámbrico.'),
    ('Teclado', 'Un teclado mecánico retroiluminado.')
]

# Limpiar la tabla antes de insertar para evitar duplicados en ejecuciones repetidas
cursor.execute("DELETE FROM items") 
cursor.executemany("INSERT INTO items (name, description) VALUES (?, ?)", items_to_insert)

print("Base de datos 'test.db' creada y poblada con éxito.")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()