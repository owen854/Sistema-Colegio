import tkinter as tk
from tkinter import ttk
import utileria.generic as utl

class FormRegisterDesigner():

    def __init__(self):
        
        self.ventana = tk.Toplevel()
        self.ventana.title('Registro de usuario')        
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 600, 500)  # Ajustar el tamaño de la ventana

        logo = utl.leer_imagen("./imagenes/logou.png", (150, 150))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg='#003366')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#003366')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=(
            'Times', 24), fg="#666a88", bg='#fcfcfc', pady=20)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=5)

        etiqueta_rol = tk.Label(frame_form_fill, text="Rol", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_rol.pack(fill=tk.X, padx=20, pady=5)
        self.role = ttk.Combobox(frame_form_fill, font=('Times', 14), values=["Estudiante", "Docente"])
        self.role.pack(fill=tk.X, padx=20, pady=5)
        self.role.current(0)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=5)
        self.password.config(show="*")
        
        etiqueta_confirmation = tk.Label(frame_form_fill, text="Confirmación", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_confirmation.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.confirmation.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Registrar", font=(
            'Times', 15), bg='#F87474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=10)
        inicio.bind("<Return>", (lambda event: self.register()))

        self.ventana.mainloop()

    def register(self):
        pass
    
    
if __name__ == "__main__":
    app = FormRegisterDesigner()
