# -*- coding: utf-8 -*-
"""actividad3.ipynb

Original file is located at
    https://colab.research.google.com/drive/1iojmyNHvXLWAPN5LscPjofljUgYgu85X
"""

numero = int(input("introduce un número: "))
if numero % 2 == 0:
  print("el número es par.")
else:
  print("el número es impar.")
print("el número es impar.")

a, b = 0, 1
for i in range(10):
print(a)
a, b = b, a+b

n = int(input("introduce un número: "))
suma = 0
for i in range(1, n+1):
suma += i
print(f"la suma de los números del 1 al {n} es: {suma}")
