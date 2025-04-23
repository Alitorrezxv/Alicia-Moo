# -*- coding: utf-8 -*-
"""actividad6.ipynb


Original file is located at
    https://colab.research.google.com/drive/1iojmyNHvXLWAPN5LscPjofljUgYgu85X
"""

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("No puedes dividir por cero.")
except ValueError:
    print("Debes ingresar números válidos.")

try:
    f = open("archivo_noexiste.txt", "r")
except FileNotFoundError:
    print("Error: No se pudo abrir el archivo.")
else:
    print("Archivo abierto correctamente.")
    f.close()
