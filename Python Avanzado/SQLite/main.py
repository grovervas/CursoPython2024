import sqlite3

# Conectar a la base de datos SQLite (crea la base de datos si no existe)
conn = sqlite3.connect('prueba.db')
cursor = conn.cursor()

# Crear la tabla persona si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS persona2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')
conn.commit()

# Función para crear un nuevo registro
def crear_persona(nombre, edad):
    cursor.execute("INSERT INTO persona2 (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    print("Persona creada exitosamente.")

# Función para leer todos los registros
def leer_personas():
    cursor.execute("SELECT * FROM persona2")
    personas = cursor.fetchall()
    print("Lista de personas:")
    for persona in personas:
        print(persona)

# Función para actualizar un registro existente
def actualizar_persona(id, nuevo_nombre, nueva_edad):
    cursor.execute("UPDATE persona2 SET nombre = ?, edad = ? WHERE id = ?", (nuevo_nombre, nueva_edad, id))
    conn.commit()
    print("Persona actualizada exitosamente.")

# Función para eliminar un registro por ID
def eliminar_persona(id):
    cursor.execute("DELETE FROM persona2 WHERE id = ?", (id,))
    conn.commit()
    print("Persona eliminada exitosamente.")

# Ejemplos de uso
# Crear una nueva persona
# crear_persona("Ana", 30)

# Actualizar una persona con id=1
actualizar_persona(2, "Lili", 31)

# Eliminar una persona con id=1
#eliminar_persona(1)

# Leer todas las personas
leer_personas()

# Cerrar la conexión
conn.close()
