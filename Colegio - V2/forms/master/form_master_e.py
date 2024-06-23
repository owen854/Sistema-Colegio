import tkinter as tk
from tkinter.font import BOLD
from tkinter import font, messagebox
from persistence.db_manager import DBManager
import utileria.generic as utl
from forms.login.form_login import FormLogin

class MasterPanelEstudiante(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestion de Cursos - Estudiante')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#fcfcfc')
        self.resizable(width=0, height=0)
        
        self.db_manager = DBManager()
        
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        
        self.asignaturas_estudiante = []  # Inicialmente vacío
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

        self.labelUsuario = tk.Label(self.barra_superior, text="Estudiante")
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
            ("Informacion Personal", "\uf007", self.abrir_informacion_personal),
            ("Asignaturas", "\uf02d", self.abrir_asignaturas),
            ("Cursos y Horarios", "\uf073 ", self.abrir_cursos),
            ("Ver Notas", "\uf091", self.abrir_ver_notas),
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

    def abrir_informacion_personal(self):
        print("Dashboard button clicked")

    def abrir_asignaturas(self):
        self.limpiar_panel(self.cuerpo_principal)
        
        label_titulo = tk.Label(self.cuerpo_principal, text="Asignaturas", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        btn_mostrar_asignaturas = tk.Button(self.cuerpo_principal, text="Mostrar Asignaturas Disponibles", 
                                            command=self.mostrar_asignaturas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_asignaturas.pack(pady=5)

        self.listbox_asignaturas = tk.Listbox(self.cuerpo_principal, selectmode=tk.MULTIPLE, font=("Roboto", 12))
        self.listbox_asignaturas.pack(pady=5, fill=tk.BOTH, expand=False)

        btn_registrar_asignaturas = tk.Button(self.cuerpo_principal, text="Registrar Asignaturas Seleccionadas", 
                                              command=self.registrar_asignaturas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_registrar_asignaturas.pack(pady=10)

    def mostrar_asignaturas(self):
        self.listbox_asignaturas.delete(0, tk.END)
        asignaturas = self.db_manager.obtener_asignaturas()
        for asignatura in asignaturas:
            self.listbox_asignaturas.insert(tk.END, asignatura[1])

    def registrar_asignaturas(self):
        seleccionadas = self.listbox_asignaturas.curselection()
        for i in seleccionadas:
            asignatura = self.listbox_asignaturas.get(i)
            if asignatura not in self.asignaturas_estudiante:
                self.asignaturas_estudiante.append(asignatura)
        messagebox.showinfo("Registro Exitoso", "Asignaturas registradas exitosamente.")

    def abrir_cursos(self):
        self.limpiar_panel(self.cuerpo_principal)
        
        label_titulo = tk.Label(self.cuerpo_principal, text="Cursos", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        btn_mostrar_registradas = tk.Button(self.cuerpo_principal, text="Mostrar Asignaturas Registradas", 
                                            command=self.mostrar_asignaturas_registradas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_registradas.pack(pady=5)

        self.listbox_asignaturas_registradas = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_asignaturas_registradas.pack(pady=5, fill=tk.BOTH, expand=False)

        btn_mostrar_info = tk.Button(self.cuerpo_principal, text="Mostrar Información del Curso", 
                                     command=self.mostrar_info_curso, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_info.pack(pady=10)

    def mostrar_asignaturas_registradas(self):
        self.listbox_asignaturas_registradas.delete(0, tk.END)
        for asignatura in self.asignaturas_estudiante:
            self.listbox_asignaturas_registradas.insert(tk.END, asignatura)

    def mostrar_info_curso(self):
        seleccionadas = self.listbox_asignaturas_registradas.curselection()
        if not seleccionadas:
            messagebox.showerror("Error", "Debe seleccionar un curso.")
            return
        asignatura = self.listbox_asignaturas_registradas.get(seleccionadas[0])
        messagebox.showinfo("Información del Curso", f"Información del curso de {asignatura}")

    def abrir_ver_notas(self):
        self.limpiar_panel(self.cuerpo_principal)
        
        label_titulo = tk.Label(self.cuerpo_principal, text="Ver Notas", font=("Roboto", 20, BOLD), bg="#f1faff")
        label_titulo.pack(pady=10)

        self.listbox_notas = tk.Listbox(self.cuerpo_principal, font=("Roboto", 12))
        self.listbox_notas.pack(pady=5, fill=tk.BOTH, expand=False)

        btn_mostrar_notas = tk.Button(self.cuerpo_principal, text="Mostrar Notas", 
                                      command=self.mostrar_notas, font=("Roboto", 12), bg="#1f2329", fg="white")
        btn_mostrar_notas.pack(pady=10)

    def mostrar_notas(self):
        self.listbox_notas.delete(0, tk.END)
        for asignatura in self.asignaturas_estudiante:
            asignatura_id = self.db_manager.obtener_asignatura_id_por_nombre(asignatura)
            notas = self.db_manager.obtener_notas(asignatura_id)
            for estudiante, nota in notas:
                self.listbox_notas.insert(tk.END, f"{asignatura} - {estudiante}: {nota}")

    def sign_out(self):
        self.destroy()
        FormLogin()

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
