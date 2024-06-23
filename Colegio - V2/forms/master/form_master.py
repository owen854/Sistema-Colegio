import tkinter as tk
from tkinter.font import BOLD
from tkinter import font, messagebox
import utileria.generic as utl
from forms.login.form_login import FormLogin


import tkinter as tk
from tkinter import messagebox, ttk, font
from persistence.db_manager import DBManager
import utileria.generic as utl

class MasterPanel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestion de Cursos - Administrador')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#fcfcfc')
        self.resizable(width=0, height=0)
        
        self.db_manager = DBManager()
        
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
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

        self.labelUsuario = tk.Label(self.barra_superior, text="Administrador")
        self.labelUsuario.config(fg="#fff", font=("Roboto", 15), bg="#1f2329", pady=10)
        self.labelUsuario.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.perfil = utl.leer_imagen("./imagenes/logou.png", (100, 100))

        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg="#2a3138")
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        buttons_info = [
            ("Gestionar Asignaturas", "\uf02d", self.abrir_gestion_asignaturas),
            ("Gestionar Estudiantes", "\uf007", self.abrir_gestion_estudiantes),
            ("Cerrar Sesion", "\uf08b", self.sign_out)
        ]

        for text, icon, command in buttons_info:
            button = tk.Button(self.menu_lateral, text=f"{icon} {text}", font=font_awesome, 
                               width=ancho_menu, height=alto_menu, bg="#2a3138", fg="white", 
                               bd=0, command=command)
            button.pack(side=tk.TOP, fill="x", pady=5)

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    def abrir_gestion_asignaturas(self):
        self.limpiar_panel(self.cuerpo_principal)
        
        label_titulo = tk.Label(self.cuerpo_principal, text="Gestionar Asignaturas", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        label_nombre = tk.Label(self.cuerpo_principal, text="Nombre de la Asignatura:", font=("Roboto", 12), bg="#f1faff")
        label_nombre.pack(pady=5)
        self.entry_nombre_asignatura = tk.Entry(self.cuerpo_principal, font=("Roboto", 12))
        self.entry_nombre_asignatura.pack(pady=5)

        btn_agregar_asignatura = tk.Button(self.cuerpo_principal, text="Agregar Asignatura", 
                                           command=self.agregar_asignatura, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_agregar_asignatura.pack(pady=10)

        self.listbox_asignaturas = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_asignaturas.pack(pady=5, fill=tk.BOTH, expand=False
        )

        btn_mostrar_asignaturas = tk.Button(self.cuerpo_principal, text="Mostrar Asignaturas", 
                                            command=self.mostrar_asignaturas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_asignaturas.pack(pady=10)

    def agregar_asignatura(self):
        nombre = self.entry_nombre_asignatura.get()
        if nombre:
            self.db_manager.insertar_asignatura(nombre)
            messagebox.showinfo("Exito", "Asignatura agregada exitosamente.")
            self.entry_nombre_asignatura.delete(0, tk.END)
            self.mostrar_asignaturas()
        else:
            messagebox.showerror("Error", "El nombre de la asignatura no puede estar vacío.")

    def mostrar_asignaturas(self):
        self.listbox_asignaturas.delete(0, tk.END)
        asignaturas = self.db_manager.obtener_asignaturas()
        for asignatura in asignaturas:
            self.listbox_asignaturas.insert(tk.END, asignatura[1])

    def abrir_gestion_estudiantes(self):
        self.limpiar_panel(self.cuerpo_principal)
        
        label_titulo = tk.Label(self.cuerpo_principal, text="Gestionar Estudiantes", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        label_nombre = tk.Label(self.cuerpo_principal, text="Nombre del Estudiante:", font=("Roboto", 12), bg="#f1faff")
        label_nombre.pack(pady=5)
        self.entry_nombre_estudiante = tk.Entry(self.cuerpo_principal, font=("Roboto", 12))
        self.entry_nombre_estudiante.pack(pady=5)

        btn_agregar_estudiante = tk.Button(self.cuerpo_principal, text="Agregar Estudiante", 
                                           command=self.agregar_estudiante, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_agregar_estudiante.pack(pady=10)

        self.listbox_estudiantes = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_estudiantes.pack(pady=5, fill=tk.BOTH, expand=False)

        btn_mostrar_estudiantes = tk.Button(self.cuerpo_principal, text="Mostrar Estudiantes", 
                                            command=self.mostrar_estudiantes, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_estudiantes.pack(pady=10)

    def agregar_estudiante(self):
        nombre = self.entry_nombre_estudiante.get()
        if nombre:
            self.db_manager.insertar_estudiante(nombre)
            messagebox.showinfo("Exito", "Estudiante agregado exitosamente.")
            self.entry_nombre_estudiante.delete(0, tk.END)
            self.mostrar_estudiantes()
        else:
            messagebox.showerror("Error", "El nombre del estudiante no puede estar vacío.")

    def mostrar_estudiantes(self):
        self.listbox_estudiantes.delete(0, tk.END)
        estudiantes = self.db_manager.obtener_estudiantes()
        for estudiante in estudiantes:
            self.listbox_estudiantes.insert(tk.END, estudiante[1])

    def sign_out(self):
        self.destroy()
        FormLogin()

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
