# -*- coding: utf-8 -*-
"""actividad5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iojmyNHvXLWAPN5LscPjofljUgYgu85X
"""

calificaciones = {
"matemáticas": 90,
"historia": 85,
"física": 78,
"química": 93
}
promedio = sum(calificaciones.values()) / len(calificaciones)
print(f"El promedio es: {promedio}")