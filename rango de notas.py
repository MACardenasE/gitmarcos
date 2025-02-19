"""
Programa que muesta el mensaje
del tipo de calificación de acuerdo
al valor de notas que tenga


nota = int(input("Ingrese nota a calificar: "))
"""

import os
limpiar = os.system('cls')

nota = 110
limpiar

if nota < 60:
    print("")
    print("Está Reprobado")
    print("")
    print("")
elif nota >= 60 and nota <= 79:
    print("")
    print("Nota Regular")
    print("")
    print("")
elif nota >= 80 and nota <= 89:
    print("")
    print("Nota Buena")
    print("")
    print("")
elif nota >= 90 and nota <= 94:
    print("")
    print("Nota Muy Buena")
    print("")
    print("")
elif nota > 94 and nota <= 100:
    print("")
    print("Nota Excelente")
    print("")
    print("")
else:
    print("")
    print("Nota NO REGISTRADA")
    print("")
    print("")



