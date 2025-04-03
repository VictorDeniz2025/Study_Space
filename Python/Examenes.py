def realizar_examen():
    print("Bienvenido al examen sobre tipos de datos en Python.")
    print("Responde las siguientes preguntas de selección múltiple.\n")

    # Preguntas y opciones
    preguntas = [
        {
            "pregunta": "1. ¿Qué tipo de dato es el resultado de la operación 5 / 2 en Python?",
            "opciones": ["a) int", "b) float", "c) str", "d) bool"],
            "respuesta": "b"
        },
        {
            "pregunta": "2. ¿Cuál de los siguientes es un tipo de dato inmutable en Python?",
            "opciones": ["a) list", "b) dict", "c) tuple", "d) set"],
            "respuesta": "c"
        },
        {
            "pregunta": "3. ¿Qué tipo de dato representa el valor True en Python?",
            "opciones": ["a) int", "b) float", "c) bool", "d) str"],
            "respuesta": "c"
        },
        {
            "pregunta": "4. ¿Qué tipo de dato es el resultado de la expresión '5' + '5'?",
            "opciones": ["a) int", "b) float", "c) str", "d) bool"],
            "respuesta": "c"
        },
        {
            "pregunta": "5. ¿Qué tipo de dato es una clave en un diccionario?",
            "opciones": ["a) Cualquier tipo mutable", "b) Cualquier tipo inmutable", "c) Solo cadenas", "d) Solo enteros"],
            "respuesta": "b"
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
        print("¡Excelente trabajo! Conoces muy bien los tipos de datos en Python.")
    elif correctas >= len(preguntas) // 2:
        print("Buen intento, pero puedes mejorar.")
    else:
        print("Necesitas estudiar más sobre los tipos de datos en Python.")

# Ejecutar el examen
if __name__ == "__main__":
    realizar_examen()