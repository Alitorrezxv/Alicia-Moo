# -*- coding: utf-8 -*-
"""actividad8.ipynb

Original file is located at
    https://colab.research.google.com/drive/1iojmyNHvXLWAPN5LscPjofljUgYgu85X
"""

tareas = ["Comprar leche", "Estudiar Python", "Hacer ejercicio"]
with open("tareas.txt", "w") as archivo:
    for tarea in tareas:
        archivo.write(tarea + "\n")
class medicamento(generico):
    def __init__(self, sustancia, nomcomer, gramaje, grupo, precio):
        super().__init__(sustancia, nomcomer)
        self.tylenol = tylelol
    
    def presentarse(self):
        return f"El medicamento {self.sustancia}, de la marca {self.nomcomer} tiene un gramaje de {self.gramaje} es de la fraccion
        {self.grupo} con un precio de {self.precio}."

para = medicameno("Paracetamol", "Tylenol", 500, "VI", 105)
print(para.medicamento())
