import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

class DropoutPredictor:
    def entrenar_modelo(self, data):
        X = data.drop(columns=["abandono"])
        y = data["abandono"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
        modelo = DecisionTreeClassifier(random_state=42)
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)
        precision = accuracy_score(y_test, y_pred)
        print(f"Precisión del modelo: {precision:.2f}")
        print("Reporte de clasificación:")
        print(classification_report(y_test, y_pred))
        return modelo

    def predecir(self, modelo, nuevo_estudiante):
        pred = modelo.predict([nuevo_estudiante])[0]
        return pred

class DropoutExample:
    def run(self):
        np.random.seed(42)
        n = 100
        data = pd.DataFrame({
            "edad": np.random.randint(18, 30, n),
            "horas_estudio": np.random.randint(0, 20, n),
            "asistencia": np.random.randint(50, 100, n),
            "promedio": np.round(np.random.uniform(5, 10, n), 2),
            "uso_plataforma": np.random.randint(0, 2, n),
        })
        # Regla simple para abandono
        data["abandono"] = ((data["asistencia"] < 70) | (data["promedio"] < 6) | (data["horas_estudio"] < 5)).astype(int)
        predictor = DropoutPredictor()
        modelo = predictor.entrenar_modelo(data)
        nuevo_estudiante = [20, 10, 80, 7.5, 1]  # edad, horas_estudio, asistencia, promedio, uso_plataforma
        resultado = predictor.predecir(modelo, nuevo_estudiante)
        print("\nEl estudiante probablemente:", "Abandonará" if resultado == 1 else "Seguirá estudiando")
