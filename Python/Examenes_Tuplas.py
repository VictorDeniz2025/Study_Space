def realizar_examen_tuplas():
    print("Bienvenido al examen sobre tuplas en Python.")
    print("Responde las siguientes preguntas de selección múltiple.\n")

    # Preguntas y opciones
    preguntas = [
        {
            "pregunta": "1. ¿Qué es una tupla en Python?",
            "opciones": [
                "a) Una colección ordenada y mutable.",
                "b) Una colección ordenada e inmutable.",
                "c) Una colección desordenada y mutable.",
                "d) Una colección desordenada e inmutable."
            ],
            "respuesta": "b"
        },
        {
            "pregunta": "2. ¿Cómo se define una tupla vacía?",
            "opciones": [
                "a) []",
                "b) {}",
                "c) ()",
                "d) None"
            ],
            "respuesta": "c"
        },
        {
            "pregunta": "3. ¿Cuál de las siguientes operaciones no es válida para una tupla?",
            "opciones": [
                "a) Acceder a un elemento por índice.",
                "b) Modificar un elemento.",
                "c) Concatenar dos tuplas.",
                "d) Verificar si un elemento está en la tupla."
            ],
            "respuesta": "b"
        },
        {
            "pregunta": "4. ¿Qué devuelve la función `len()` cuando se aplica a una tupla?",
            "opciones": [
                "a) El número de elementos en la tupla.",
                "b) El tamaño en bytes de la tupla.",
                "c) La suma de los elementos de la tupla.",
                "d) Ninguna de las anteriores."
            ],
            "respuesta": "a"
        },
        {
            "pregunta": "5. ¿Qué sucede si intentas modificar un elemento de una tupla?",
            "opciones": [
                "a) Se modifica el elemento.",
                "b) Se lanza un error.",
                "c) Se crea una nueva tupla.",
                "d) No sucede nada."
            ],
            "respuesta": "b"
        },
        {
            "pregunta": "6. ¿Cómo se accede al último elemento de una tupla?",
            "opciones": [
                "a) tuple[-1]",
                "b) tuple[len(tuple)]",
                "c) tuple[last]",
                "d) Ninguna de las anteriores."
            ],
            "respuesta": "a"
        },
        {
            "pregunta": "7. ¿Qué operador se usa para concatenar dos tuplas?",
            "opciones": [
                "a) +",
                "b) *",
                "c) &",
                "d) |"
            ],
            "respuesta": "a"
        },
        {
            "pregunta": "8. ¿Qué método se usa para contar cuántas veces aparece un elemento en una tupla?",
            "opciones": [
                "a) count()",
                "b) index()",
                "c) find()",
                "d) search()"
            ],
            "respuesta": "a"
        },
        {
            "pregunta": "9. ¿Qué método se usa para encontrar el índice de un elemento en una tupla?",
            "opciones": [
                "a) count()",
                "b) index()",
                "c) find()",
                "d) search()"
            ],
            "respuesta": "b"
        },
        {
            "pregunta": "10. ¿Es posible tener una tupla dentro de otra tupla?",
            "opciones": [
                "a) Sí.",
                "b) No.",
                "c) Solo si ambas tuplas son del mismo tamaño.",
                "d) Solo si las tuplas contienen números."
            ],
            "respuesta": "a"
        }
    ]

    # Contador de respuestas correctas
    correctas = 0

    # Iterar sobre las preguntas
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta_usuario = input("Tu respuesta: ").lower()

        if respuesta_usuario == pregunta["respuesta"]:
            print("¡Correcto!\n")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}\n")

    # Resultados finales
    print(f"Examen finalizado. Respuestas correctas: {correctas} de {len(preguntas)}.")
    if correctas == len(preguntas):
        print("¡Excelente trabajo! Conoces muy bien las tuplas en Python.")
    elif correctas >= len(preguntas) // 2:
        print("Buen intento, pero puedes mejorar.")
    else:
        print("Necesitas estudiar más sobre las tuplas en Python.")

# Ejecutar el examen
if __name__ == "__main__":
    realizar_examen_tuplas()