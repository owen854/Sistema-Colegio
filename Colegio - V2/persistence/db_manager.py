import sqlite3

class DBManager:
    def __init__(self, db_name='gestion_cursos.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS asignaturas (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS notas (
                    id INTEGER PRIMARY KEY,
                    estudiante_id INTEGER,
                    asignatura_id INTEGER,
                    nota REAL,
                    FOREIGN KEY (estudiante_id) REFERENCES estudiantes (id),
                    FOREIGN KEY (asignatura_id) REFERENCES asignaturas (id)
                )
            ''')

    def insertar_asignatura(self, nombre):
        with self.connection:
            self.connection.execute('INSERT INTO asignaturas (nombre) VALUES (?)', (nombre,))

    def obtener_asignaturas(self):
        with self.connection:
            return self.connection.execute('SELECT * FROM asignaturas').fetchall()

    def insertar_estudiante(self, nombre):
        with self.connection:
            self.connection.execute('INSERT INTO estudiantes (nombre) VALUES (?)', (nombre,))

    def obtener_estudiantes(self):
        with self.connection:
            return self.connection.execute('SELECT * FROM estudiantes').fetchall()

    def insertar_nota(self, estudiante_id, asignatura_id, nota):
        with self.connection:
            self.connection.execute('''
                INSERT INTO notas (estudiante_id, asignatura_id, nota) 
                VALUES (?, ?, ?)
            ''', (estudiante_id, asignatura_id, nota))

    def obtener_notas(self, asignatura_id):
        with self.connection:
            return self.connection.execute('''
                SELECT e.nombre, n.nota
                FROM notas n
                JOIN estudiantes e ON n.estudiante_id = e.id
                WHERE n.asignatura_id = ?
            ''', (asignatura_id,)).fetchall()

    def close(self):
        self.connection.close()
