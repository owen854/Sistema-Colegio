import tkinter as tk
from tkinter.font import BOLD
from tkinter import font, messagebox
import utileria.generic as utl
from forms.login.form_login import FormLogin


class MasterPanel(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Gestion de Cursos - Docente')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#fcfcfc')
        self.resizable(width=0, height=0)
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.asignaturas_disponibles = ["Calculo I", "Física", "Programacion Lineal"]
        self.asignaturas_docente = []  # Inicialmente vacío
        self.informacion_asignaturas = {
            "Calculo I": {"horario": "Lunes 10-12", "Estudiantes": "N/A"},
            "Física": {"horario": "Martes 14-16", "Estudiantes": "N/A"},
            "Programacion Lineal": {"horario": "Miércoles 8-10", "Estudiantes": "N/A",}
        }
        self.notas_estudiantes = {}  # Diccionario para almacenar notas de estudiantes
        self.mainloop()

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg="#1f2329", height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg="#2a3138", width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(self, bg="#f1faff")
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Plataforma")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg="#1f2329", pady=10)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg="#1f2329", fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelUsuario = tk.Label(self.barra_superior, text="Profesor")
        self.labelUsuario.config(fg="#fff", font=("Roboto", 15), bg="#1f2329", pady=10)
        self.labelUsuario.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        # Placeholder image for profile
        # Replace with your actual image path and loading mechanism
        self.perfil = utl.leer_imagen("./imagenes/logou.png", (100, 100))

        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg="#2a3138")
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        buttons_info = [
            ("Informacion Personal", "\uf007", self.abrir_informacion_personal),
            ("Asignaturas", "\uf02d", self.abrir_asignaturas),
            ("Cursos", "\uf073", self.abrir_cursos),
            ("Registrar Notas", "\uf081", self.abrir_registrar_notas),
            ("Cerrar Sesion", "\uf08b", self.sign_out)
        ]

        for text, icon, command in buttons_info:
            button = tk.Button(self.menu_lateral, text=f"{icon} {text}", font=font_awesome, 
                               width=ancho_menu, height=alto_menu, bg="#2a3138", fg="white", 
                               bd=0, command=command)
            button.pack(side=tk.TOP, fill="x", pady=5)

    def toggle_panel(self):
        # Function to toggle the visibility of the side menu
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    def abrir_informacion_personal(self):
        # Placeholder for the actual dashboard button command
        print("Dashboard button clicked")

    def abrir_asignaturas(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Título
        label_titulo = tk.Label(self.cuerpo_principal, text="Asignaturas", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        # Botón para mostrar asignaturas disponibles
        btn_mostrar_asignaturas = tk.Button(self.cuerpo_principal, text="Mostrar Asignaturas Disponibles", 
                                            command=self.mostrar_asignaturas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_asignaturas.pack(pady=5)

        # Listbox para seleccionar asignaturas
        self.listbox_asignaturas = tk.Listbox(self.cuerpo_principal, selectmode=tk.MULTIPLE, font=("Roboto", 12))
        self.listbox_asignaturas.pack(pady=5, fill=tk.BOTH, expand=False)

        # Botón para registrar asignaturas seleccionadas
        btn_registrar_asignaturas = tk.Button(self.cuerpo_principal, text="Registrar Asignaturas Seleccionadas", 
                                              command=self.registrar_asignaturas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_registrar_asignaturas.pack(pady=10)

    def mostrar_asignaturas(self):
        # Limpiar listbox
        self.listbox_asignaturas.delete(0, tk.END)
        
        # Mostrar asignaturas disponibles en la listbox
        for asignatura in self.asignaturas_disponibles:
            self.listbox_asignaturas.insert(tk.END, asignatura)

    def registrar_asignaturas(self):
        # Obtener asignaturas seleccionadas
        seleccionadas = self.listbox_asignaturas.curselection()
        for i in seleccionadas:
            asignatura = self.listbox_asignaturas.get(i)
            if asignatura not in self.asignaturas_docente:
                self.asignaturas_docente.append(asignatura)
                self.notas_estudiantes[asignatura] = {}  # Inicializar notas de estudiantes para la asignatura
        
        # Mostrar mensaje de éxito
        messagebox.showinfo("Registro Exitoso", "Asignaturas registradas exitosamente.")

    def abrir_cursos(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Título
        label_titulo = tk.Label(self.cuerpo_principal, text="Cursos", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        # Botón para mostrar asignaturas registradas
        btn_mostrar_registradas = tk.Button(self.cuerpo_principal, text="Mostrar Asignaturas Registradas", 
                                            command=self.mostrar_asignaturas_registradas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_registradas.pack(pady=5)

        # Listbox para mostrar asignaturas registradas
        self.listbox_asignaturas_registradas = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_asignaturas_registradas.pack(pady=5, fill=tk.BOTH, expand=False)

        # Botón para mostrar información del curso seleccionado
        btn_mostrar_info = tk.Button(self.cuerpo_principal, text="Mostrar Información", 
                                     command=self.mostrar_informacion_curso, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_info.pack(pady=5)

    def mostrar_asignaturas_registradas(self):
        # Limpiar listbox
        self.listbox_asignaturas_registradas.delete(0, tk.END)
        
        # Mostrar asignaturas registradas en la listbox
        for asignatura in self.asignaturas_docente:
            self.listbox_asignaturas_registradas.insert(tk.END, asignatura)

    def mostrar_informacion_curso(self):
        # Obtener asignatura seleccionada
        seleccion = self.listbox_asignaturas_registradas.curselection()
        if seleccion:
            asignatura = self.listbox_asignaturas_registradas.get(seleccion[0])
            info = self.informacion_asignaturas.get(asignatura, {})
            horario = info.get("horario", "No disponible")
            nota = info.get("nota", "No disponible")
            profesor = info.get("profesor", "No disponible")
            
            # Mostrar información del curso
            messagebox.showinfo("Información del Curso", f"Asignatura: {asignatura}\nHorario: {horario}\nEstudiantes: {nota}\nProfesor: {profesor}")

    def abrir_registrar_notas(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Título
        label_titulo = tk.Label(self.cuerpo_principal, text="Registrar Notas", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        # Listbox para seleccionar asignaturas registradas
        self.listbox_notas_asignaturas = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_notas_asignaturas.pack(pady=5, fill=tk.BOTH, expand=False)

        # Botón para mostrar estudiantes de la asignatura seleccionada
        btn_mostrar_estudiantes = tk.Button(self.cuerpo_principal, text="Mostrar Estudiantes", 
                                            command=self.mostrar_estudiantes, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_estudiantes.pack(pady=5)

        # Listbox para mostrar estudiantes
        self.listbox_estudiantes = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_estudiantes.pack(pady=5, fill=tk.BOTH, expand=False)

        # Entrada y botón para registrar notas
        self.entry_nota = tk.Entry(self.cuerpo_principal, font=("Roboto", 12))
        self.entry_nota.pack(pady=5)
        btn_registrar_nota = tk.Button(self.cuerpo_principal, text="Registrar Nota", 
                                       command=self.registrar_nota, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_registrar_nota.pack(pady=5)

        # Mostrar asignaturas registradas en la listbox
        self.mostrar_asignaturas_registradas_notas()

    def mostrar_asignaturas_registradas_notas(self):
        # Limpiar listbox
        self.listbox_notas_asignaturas.delete(0, tk.END)
        
        # Mostrar asignaturas registradas en la listbox
        for asignatura in self.asignaturas_docente:
            self.listbox_notas_asignaturas.insert(tk.END, asignatura)

    def mostrar_estudiantes(self):
        # Obtener asignatura seleccionada
        seleccion = self.listbox_notas_asignaturas.curselection()
        if seleccion:
            asignatura = self.listbox_notas_asignaturas.get(seleccion[0])
            estudiantes = self.notas_estudiantes.get(asignatura, {}).keys()
            
            # Limpiar listbox de estudiantes
            self.listbox_estudiantes.delete(0, tk.END)
            
            # Mostrar estudiantes en la listbox
            for estudiante in estudiantes:
                self.listbox_estudiantes.insert(tk.END, estudiante)

    def registrar_nota(self):
        # Obtener estudiante seleccionado
        seleccion = self.listbox_estudiantes.curselection()
        if seleccion:
            estudiante = self.listbox_estudiantes.get(seleccion[0])
            asignatura = self.listbox_notas_asignaturas.get(self.listbox_notas_asignaturas.curselection()[0])
            nota = self.entry_nota.get()

            # Registrar la nota del estudiante en la asignatura
            self.notas_estudiantes[asignatura][estudiante] = nota

            # Mostrar mensaje de éxito
            messagebox.showinfo("Registro Exitoso", f"Nota registrada para {estudiante} en {asignatura}")

    def sign_out(self):
        self.limpiar_panel(self.cuerpo_principal)
        # Confirmar cierre de sesión
        respuesta = messagebox.askyesno("Cerrar Sesión", "¿Está seguro que desea cerrar sesión?")
        if respuesta:
            self.destroy()
            FormLogin().mainloop()
    
    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
