import tkinter as tk
from tkinter import messagebox

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        info = f"Curso: {self.nombre}\nProfesor: {self.profesor.nombre} {self.profesor.apellido}\nHorario: {self.horario.mostrar_info()}\n"
        return info

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        info = f"Profesor: {self.nombre} {self.apellido}\nAsignaturas:\n"
        for asignatura in self.asignaturas:
            info += f"- {asignatura.nombre}\n"
        return info

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        info = f"Estudiante: {self.nombre} {self.apellido} (ID: {self.id_estudiante})\nCursos:\n"
        for curso in self.cursos:
            info += f"- {curso.nombre}\n"
        return info

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def mostrar_info(self):
        return f"Asignatura: {self.nombre}\nProfesor: {self.profesor.nombre} {self.profesor.apellido}"

class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        return f"Curso: {self.curso.nombre}\nEstudiante: {self.estudiante.nombre} {self.estudiante.apellido}\nNota: {self.nota}"

class Horario:
    def __init__(self, dias, hora_inicio, hora_fin):
        self.dias = dias
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"{self.dias}: {self.hora_inicio} - {self.hora_fin}"

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")

        self.titulo_principal = tk.Label(self.root, text="MATRICULACION DE CURSOS", font=("Arial", 16, "bold"), fg="dark blue")
        self.titulo_principal.pack(pady=10)

        
        self.profesores = [Profesor("Juan", "Pérez"), Profesor("María", "García"), Profesor("Carlos", "Hernández"),
                           Profesor("Ana", "Rodríguez"), Profesor("Luis", "Martínez"), Profesor("Elena", "Sánchez"),
                           Profesor("Marta", "González"), Profesor("Jorge", "Fernández"), Profesor("Lucía", "López")]
        self.estudiantes = [Estudiante("Pedro", "López", "001"), Estudiante("Ana", "Martínez", "002")]
        self.cursos = self.crear_cursos()
        self.cursos_disponibles = self.cursos.copy()

        
        self.crear_interfaz()

    def crear_cursos(self):
        cursos = [
            Curso("Matemáticas Avanzadas", self.profesores[0], Horario("Lunes, Miércoles, Viernes", "10:00", "11:30")),
            Curso("Física Cuántica", self.profesores[1], Horario("Martes, Jueves", "14:00", "15:30")),
            Curso("Historia del Arte", self.profesores[2], Horario("Lunes, Miércoles", "16:00", "17:30")),
            Curso("Programación en Python", self.profesores[3], Horario("Martes, Jueves", "09:00", "10:30")),
            Curso("Economía", self.profesores[4], Horario("Miércoles, Viernes", "13:00", "14:30")),
            Curso("Literatura Inglesa", self.profesores[5], Horario("Lunes, Jueves", "11:00", "12:30")),
            Curso("Biología Molecular", self.profesores[6], Horario("Martes, Viernes", "08:00", "09:30")),
            Curso("Filosofía", self.profesores[7], Horario("Lunes, Miércoles", "13:00", "14:30")),
            Curso("Química Orgánica", self.profesores[8], Horario("Martes, Jueves", "15:00", "16:30")),
        ]
        return cursos

    def crear_interfaz(self):
       
        self.boton_mostrar_cursos = tk.Button(self.root, text="Mostrar Cursos Disponibles", command=self.mostrar_ventana_cursos_disponibles)
        self.boton_mostrar_cursos.pack(pady=10)

        self.boton_mostrar_info = tk.Button(self.root, text="Mostrar Información", command=self.mostrar_info)
        self.boton_mostrar_info.pack(pady=10)
        
        self.boton_mostrar_matriculados = tk.Button(self.root, text="Mostrar Cursos Matriculados", command=self.mostrar_cursos_matriculados)
        self.boton_mostrar_matriculados.pack(pady=10)

        self.texto_info = tk.Text(self.root, width=70, height=15)
        self.texto_info.pack(pady=10)

    def mostrar_ventana_cursos_disponibles(self):
        ventana_cursos = tk.Toplevel(self.root)
        ventana_cursos.title("Cursos Disponibles")
        ventana_cursos.geometry("400x300")

        
        titulo_ventana = tk.Label(ventana_cursos, text="MATRICULACION DE CURSOS", font=("Arial", 20, "bold"), fg="dark blue")
        titulo_ventana.pack(pady=10)

        lista_cursos = tk.Listbox(ventana_cursos, selectmode=tk.SINGLE)
        lista_cursos.pack(fill=tk.BOTH, expand=True)

        for curso in self.cursos_disponibles:
            info = f"{curso.nombre} ({curso.horario.dias} {curso.horario.hora_inicio}-{curso.horario.hora_fin})"
            lista_cursos.insert(tk.END, info)

        def agregar_curso():
            seleccion = lista_cursos.curselection()
            if seleccion:
                curso_seleccionado = self.cursos_disponibles[seleccion[0]]
                estudiante = self.estudiantes[0]
                estudiante.cursos.append(curso_seleccionado)
                curso_seleccionado.estudiantes.append(estudiante)
                self.cursos_disponibles.remove(curso_seleccionado)
                messagebox.showinfo("Curso Agregado", f"El curso '{curso_seleccionado.nombre}' ha sido agregado a {estudiante.nombre} {estudiante.apellido}.")
                ventana_cursos.destroy()
            else:
                messagebox.showwarning("Advertencia", "Debe seleccionar un curso.")

        boton_agregar = tk.Button(ventana_cursos, text="Agregar Curso", command=agregar_curso)
        boton_agregar.pack(pady=10)

    def mostrar_info(self):
        self.texto_info.delete("1.0", tk.END)
        info = "Información de Cursos:\n"
        for curso in self.cursos:
            info += curso.mostrar_info() + "\n"

        self.texto_info.insert(tk.END, info)
        
    def mostrar_cursos_matriculados(self):
        self.texto_info.delete("1.0", tk.END)
        estudiante = self.estudiantes[0]
        info = f"Cursos Matriculados de {estudiante.nombre} {estudiante.apellido}:\n"
        for curso in estudiante.cursos:
            info += f"Curso: {curso.nombre}\nProfesor: {curso.profesor.nombre} {curso.profesor.apellido}\nHorario: {curso.horario.mostrar_info()}\n\n"
        self.texto_info.insert(tk.END, info)


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
