class Libro:
    biblioteca = []

    def __init__(self, titulo, autor, ISBN, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = disponible

    def agregar(self):
        Libro.biblioteca.append(self)
        print("Libro agregado con éxito")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    @staticmethod
    def mostrar():
        for libro in Libro.biblioteca:
            estado = "Sí" if libro.disponible else "No"
            print(
                f"{libro.titulo} ({libro.autor}) - ISBN: {libro.ISBN} - Disponible: {estado}")

    @staticmethod
    def buscar(ISBN):
        for libro in Libro.biblioteca:
            if libro.ISBN == ISBN:
                estado = "Sí" if libro.disponible else "No"
                print(
                    f"{libro.titulo} ({libro.autor}) - ISBN: {libro.ISBN} - Disponible: {estado}")
                return libro
        print(f"No se encontró ningún libro con ISBN: {ISBN}")
        return None


def menu():
    while True:
        print("\nMenú:")
        print("1) Agregar un nuevo libro")
        print("2) Prestar un libro")
        print("3) Devolver un libro")
        print("4) Mostrar todos los libros")
        print("5) Salir del programa")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            ISBN = input("Ingrese el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, ISBN)
            nuevo_libro.agregar()

        elif opcion == '2':
            ISBN = input("Ingrese el ISBN del libro a prestar: ")
            libro = Libro.buscar(ISBN)
            if libro:
                libro.prestar()
            else:
                print(f"No se encontró ningún libro con ISBN: {ISBN}")

        elif opcion == '3':
            ISBN = input("Ingrese el ISBN del libro a devolver: ")
            libro = Libro.buscar(ISBN)
            if libro:
                libro.devolver()
            else:
                print(f"No se encontró ningún libro con ISBN: {ISBN}")

        elif opcion == '4':
            Libro.mostrar()

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejecutar el menú
menu()
