from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, mundo desde Flask en la carpeta Pruebas!"

if __name__ == "__main__":
    app.run(debug=True)