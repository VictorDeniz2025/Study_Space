class Libro:
    # Lista de clase para almacenar todos los libros
    biblioteca = []

    def __init__(self, titulo, autor, ISBN, disponible=True):
        # Inicializa los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = disponible

    def agregar(self):
        # Agrega el libro a la lista de la biblioteca
        Libro.biblioteca.append(self)
        print("Libro agregado con éxito")

    def prestar(self):
        # Cambia el estado de disponible a False si el libro está disponible
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        # Cambia el estado de disponible a True si el libro estaba prestado
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    @staticmethod
    def mostrar():
        # Muestra todos los libros en la biblioteca con su estado
        for libro in Libro.biblioteca:
            estado = "Sí" if libro.disponible else "No"
            print(
                f"{libro.titulo} ({libro.autor}) - ISBN: {libro.ISBN} - Disponible: {estado}")

    @staticmethod
    def buscar(ISBN):
        # Busca un libro por su ISBN y lo muestra si se encuentra
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
        # Muestra el menú de opciones
        print("\nMenú:")
        print("1) Agregar un nuevo libro")
        print("2) Prestar un libro")
        print("3) Devolver un libro")
        print("4) Mostrar todos los libros")
        print("5) Salir del programa")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            # Agregar un nuevo libro
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            ISBN = input("Ingrese el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, ISBN)
            nuevo_libro.agregar()

        elif opcion == '2':
            # Prestar un libro
            ISBN = input("Ingrese el ISBN del libro a prestar: ")
            libro = Libro.buscar(ISBN)
            if libro:
                libro.prestar()
            else:
                print(f"No se encontró ningún libro con ISBN: {ISBN}")

        elif opcion == '3':
            # Devolver un libro
            ISBN = input("Ingrese el ISBN del libro a devolver: ")
            libro = Libro.buscar(ISBN)
            if libro:
                libro.devolver()
            else:
                print(f"No se encontró ningún libro con ISBN: {ISBN}")

        elif opcion == '4':
            # Mostrar todos los libros
            Libro.mostrar()

        elif opcion == '5':
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            # Opción inválida
            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejecutar el menú
menu()
