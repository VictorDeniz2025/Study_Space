from pymongo import MongoClient

# Conexión al servidor MongoDB
cliente = MongoClient("mongodb://localhost:27017/")

# Crear o acceder a la base de datos
base_de_datos = cliente["mi_base_de_datos"]

# Crear o acceder a la colección (tabla)
coleccion = base_de_datos["mi_coleccion"]

# Lista de datos de pájaros con sus localizaciones
pajaros = [
    {"nombre": "Águila calva", "localizacion": "América del Norte"},
    {"nombre": "Cóndor andino", "localizacion": "América del Sur"},
    {"nombre": "Kiwi", "localizacion": "Nueva Zelanda"},
    {"nombre": "Pingüino emperador", "localizacion": "Antártida"},
    {"nombre": "Cacatúa", "localizacion": "Australia"},
    {"nombre": "Colibrí", "localizacion": "América Central y del Sur"},
    {"nombre": "Flamenco", "localizacion": "África, América y Europa"},
    {"nombre": "Ganso de Canadá", "localizacion": "América del Norte"},
    {"nombre": "Halcón peregrino", "localizacion": "Global"},
    {"nombre": "Loro gris africano", "localizacion": "África"},
    {"nombre": "Pavo real", "localizacion": "India"},
    {"nombre": "Pelícano", "localizacion": "Global"},
    {"nombre": "Búho nival", "localizacion": "Ártico"},
    {"nombre": "Cisne", "localizacion": "Global"},
    {"nombre": "Cuervo", "localizacion": "Global"},
    {"nombre": "Gaviota", "localizacion": "Costas globales"},
    {"nombre": "Gorrión", "localizacion": "Global"},
    {"nombre": "Jilguero", "localizacion": "Europa y América"},
    {"nombre": "Martín pescador", "localizacion": "Global"},
    {"nombre": "Pato mandarín", "localizacion": "Asia"},
    {"nombre": "Pájaro carpintero", "localizacion": "Global"},
    {"nombre": "Tucán", "localizacion": "América Central y del Sur"},
    {"nombre": "Zorzal", "localizacion": "Global"},
    {"nombre": "Águila real", "localizacion": "Europa, Asia y América del Norte"},
    {"nombre": "Cernícalo", "localizacion": "Global"},
    {"nombre": "Cigüeña", "localizacion": "Global"},
    {"nombre": "Cormorán", "localizacion": "Costas globales"},
    {"nombre": "Cuclillo", "localizacion": "Global"},
    {"nombre": "Gallo de las rocas", "localizacion": "América del Sur"},
    {"nombre": "Garza", "localizacion": "Global"},
    {"nombre": "Golondrina", "localizacion": "Global"},
    {"nombre": "Grulla", "localizacion": "Global"},
    {"nombre": "Hornero", "localizacion": "América del Sur"},
    {"nombre": "Ibis", "localizacion": "Global"},
    {"nombre": "Jacana", "localizacion": "Regiones tropicales"},
    {"nombre": "Kakapo", "localizacion": "Nueva Zelanda"},
    {"nombre": "Lechuza", "localizacion": "Global"},
    {"nombre": "Mirlo", "localizacion": "Global"},
    {"nombre": "Ñandú", "localizacion": "América del Sur"},
    {"nombre": "Papamoscas", "localizacion": "Global"},
    {"nombre": "Periquito", "localizacion": "Australia"},
    {"nombre": "Petirrojo", "localizacion": "Europa y América"},
    {"nombre": "Quetzal", "localizacion": "América Central"},
    {"nombre": "Ruiseñor", "localizacion": "Europa y Asia"},
    {"nombre": "Tero", "localizacion": "América del Sur"},
    {"nombre": "Urraca", "localizacion": "Global"},
    {"nombre": "Vencejo", "localizacion": "Global"},
    {"nombre": "Yaco", "localizacion": "África"},
    {"nombre": "Zorzal patirrojo", "localizacion": "Europa y Asia"}
]

# Insertar los datos en la colección
coleccion.insert_many(pajaros)

# Confirmación de creación
print("Conexión exitosa y colección creada.")
print("50 pájaros insertados en la colección.")