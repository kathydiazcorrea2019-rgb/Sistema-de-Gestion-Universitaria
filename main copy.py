# Clase Profesor
class Profesor:
    def __init__(self, nombre, id_profesor):
        self.nombre = nombre
        self.id_profesor = id_profesor

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_profesor})"

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.cursos = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_estudiante})"

# Clase Curso
class Curso:
    def __init__(self, id_curso, nombre, profesor):
        self.id_curso = id_curso
        self.nombre = nombre
        self.profesor = profesor

        # Creacion de lista estudiantes matriculados
        self.estudiantes = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_curso}) - Profesor: {self.profesor.nombre}"

# Funciones agregadas al sistema

# Matricular al Estudiante
def matricular_estudiante(estudiante, curso):

# Verificamos que el estudiante ya este matriculado
    if estudiante in curso.estudiantes:
        print("El estudiante ya esta matriculado en este curso.")
        return

# Validacion de la nota
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0 - 5): "))

            if 0 <= nota <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5")

        except ValueError:
            print("Debe ingresar un numero correcto")

# Guardar curso y nota
    estudiante.cursos.append({"curso": curso, "nota": nota})
# Agregar estudiante al curso
    curso.estudiantes.append(estudiante)

    print("Estudiante matriculado correctamente")

# Calcular el promedio
def calcular_promedio(estudiante):

    if not estudiante.cursos:
        print("El estudiante no tiene cursos registrados.")
        return

    suma = 0

    for c in estudiante.cursos:
        suma += c["nota"]

    promedio = suma / len(estudiante.cursos)

    print("El promedio de", estudiante.nombre, "es:", round(promedio, 2))


# Mostrar estudiantes de un curso
def mostrar_estudiantes_curso(curso):

    print("\nCurso:", curso.nombre)
    print("Profesor:", curso.profesor.nombre)

    if not curso.estudiantes:
        print("No hay estudiantes matriculados.")
        return

    print("Estudiantes inscritos:")

    for est in curso.estudiantes:
        print("-", est.nombre)


# Programa principal

def main():

    estudiantes = []
    profesores = []
    cursos = []

    while True:

        print("\nSistema de Gestion Universitaria")
        print("1. Registrar estudiante")
        print("2. Registrar profesor")
        print("3. Registrar curso")
        print("4. Matricular estudiante en curso")
        print("5. Calcular promedio de un estudiante")
        print("6. Ver estudiantes de un curso")
        print("7. Ver lista de estudiantes")
        print("8. Ver lista de cursos")
        print("9. Salir")

        opc = input("Seleccione una opcion: ")

# Registrar estudiante
        if opc == "1":

            nombre = input("Nombre del estudiante: ")
            id_est = input("ID del estudiante: ")

            estudiante = Estudiante(nombre, id_est)
            estudiantes.append(estudiante)

            print("Estudiante registrado correctamente.")

# Registrar Profesor
        elif opc == "2":

            nombre = input("Nombre del profesor: ")
            id_prof = input("ID del profesor: ")

            profesor = Profesor(nombre, id_prof)
            profesores.append(profesor)

            print("Profesor registrado correctamente.")

# Registar curso
        elif opc == "3":

            if not profesores:
                print("Primero debe registrar un profesor.")
                continue

            id_curso = input("ID del curso: ")
            nombre_curso = input("Nombre del curso: ")

            print("\nProfesores disponibles:")
            for prof in profesores:
                print(prof.id_profesor, "-", prof.nombre)

            id_prof_sel = input("Ingrese el ID del profesor: ")

            profesor_seleccionado = None

            for prof in profesores:
                if prof.id_profesor == id_prof_sel:
                    profesor_seleccionado = prof
                    break

            if profesor_seleccionado:

                curso = Curso(id_curso, nombre_curso, profesor_seleccionado)
                cursos.append(curso)

                print("Curso registrado correctamente.")

            else:
                print("Profesor no encontrado.")

# Matricular estudiante
        elif opc == "4":

            if not estudiantes or not cursos:
                print("Debe existir al menos un estudiante y un curso.")
                continue

            print("\nEstudiantes disponibles:")
            for est in estudiantes:
                print(est.id_estudiante, "-", est.nombre)

            id_est = input("Ingrese el ID del estudiante: ")

            print("\nCursos disponibles:")
            for cur in cursos:
                print(cur.id_curso, "-", cur.nombre)

            id_curso = input("Ingrese el ID del curso: ")

            estudiante_sel = None
            curso_sel = None

            for est in estudiantes:
                if est.id_estudiante == id_est:
                    estudiante_sel = est
                    break

            for cur in cursos:
                if cur.id_curso == id_curso:
                    curso_sel = cur
                    break

            if estudiante_sel and curso_sel:
                matricular_estudiante(estudiante_sel, curso_sel)
            else:
                print("No se encontro el estudiante o el curso.")

# Calcular Promedio
        elif opc == "5":

            id_est = input("Ingrese el ID del estudiante: ")

            estudiante_sel = None

            for est in estudiantes:
                if est.id_estudiante == id_est:
                    estudiante_sel = est
                    break

            if estudiante_sel:
                calcular_promedio(estudiante_sel)
            else:
                print("Estudiante no encontrado.")

# Ver estudiante de un curso
        elif opc == "6":

            id_curso = input("Ingrese el ID del curso: ")

            curso_sel = None

            for cur in cursos:
                if cur.id_curso == id_curso:
                    curso_sel = cur
                    break

            if curso_sel:
                mostrar_estudiantes_curso(curso_sel)
            else:
                print("Curso no encontrado.")

# Mostrar la lista de estudiantes
        elif opc == "7":

            print("\nLista de estudiantes:")
            for est in estudiantes:
                print(est)

# Mostrar la lista de cursos
        elif opc == "8":

            print("\nLista de cursos:")
            for cur in cursos:
                print(cur)


        elif opc == "9":

            print("Fin del programa.")
            break

        else:
            print("Opcion incorrecta.")


# ejecucion del programa
if __name__ == "__main__":
    main()
