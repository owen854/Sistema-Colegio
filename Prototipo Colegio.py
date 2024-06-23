import tkinter as tk
from tkinter import ttk

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        info = f"Curso: {self.nombre}\n"
        info += f"Profesor: {self.profesor.nombre} {self.profesor.apellido}\n"
        info += "Estudiantes:\n"
        for estudiante in self.estudiantes:
            info += f"- {estudiante.nombre} {estudiante.apellido}\n"
        info += "Horario:\n"
        info += self.horario.mostrar_info()
        return info

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.cursos.append(self)

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        info = f"Profesor: {self.nombre} {self.apellido}\n"
        info += "Asignaturas:\n"
        for asignatura in self.asignaturas:
            info += f"- {asignatura}\n"
        return info

    def asignar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        info = f"Estudiante: {self.nombre} {self.apellido}\n"
        info += f"ID de estudiante: {self.id_estudiante}\n"
        info += "Cursos:\n"
        for curso in self.cursos:
            info += f"- {curso.nombre}\n"
        return info

class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        info = "Evaluación:\n"
        info += f"Curso: {self.curso.nombre}\n"
        info += f"Estudiante: {self.estudiante.nombre} {self.estudiante.apellido}\n"
        info += f"Nota: {self.nota}\n"
        return info

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        info = f"Horario:\n"
        info += f"Día: {self.dia}\n"
        info += f"Hora de inicio: {self.hora_inicio}\n"
        info += f"Hora de fin: {self.hora_fin}\n"
        return info

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Cursos")

        self.profesor = Profesor("Juan", "Pérez")
        self.curso = Curso("Cálculo I", self.profesor, Horario("Lunes", "8:00", "9:30"))
        self.profesor.asignar_asignatura("Cálculo I")
        self.estudiante = Estudiante("María", "Gómez", 12345)
        self.curso.agregar_estudiante(self.estudiante)
        self.evaluacion = Evaluacion(self.curso, self.estudiante, 9.5)

        self.create_widgets()

    def create_widgets(self):
        self.tabs = ttk.Notebook(self)
        
        self.tab_profesor = ttk.Frame(self.tabs)
        self.tab_curso = ttk.Frame(self.tabs)
        self.tab_estudiante = ttk.Frame(self.tabs)
        self.tab_evaluacion = ttk.Frame(self.tabs)
        
        self.tabs.add(self.tab_profesor, text='Profesor')
        self.tabs.add(self.tab_curso, text='Curso')
        self.tabs.add(self.tab_estudiante, text='Estudiante')
        self.tabs.add(self.tab_evaluacion, text='Evaluación')
        
        self.tabs.pack(expand=1, fill="both")

        self.profesor_info = tk.Text(self.tab_profesor, height=10, width=50)
        self.profesor_info.pack()
        self.profesor_info.insert(tk.END, self.profesor.mostrar_info())

        self.curso_info = tk.Text(self.tab_curso, height=15, width=50)
        self.curso_info.pack()
        self.curso_info.insert(tk.END, self.curso.mostrar_info())

        self.estudiante_info = tk.Text(self.tab_estudiante, height=10, width=50)
        self.estudiante_info.pack()
        self.estudiante_info.insert(tk.END, self.estudiante.mostrar_info())

        self.evaluacion_info = tk.Text(self.tab_evaluacion, height=10, width=50)
        self.evaluacion_info.pack()
        self.evaluacion_info.insert(tk.END, self.evaluacion.mostrar_info())

if __name__ == "__main__":
    app = App()
    app.mainloop()
