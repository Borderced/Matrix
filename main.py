import numpy as np
from fractions import Fraction
from colorama import Fore,Back
import os


# Declaracion de funciones


# Esta funcion sirve para limpiar la consola despues de seleccionar "Sacar otra matriz" en cualquier Sistema Operativo
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")




copy = """

     <----------------------------------------- ORIGINAL CODE BY BORDERCED ----------------------------------------->


"""

menu2 = """

¡HOLA! Bienvenido a la calculadora de matrices, a continuacion ingresa las filas y columnas de tu sistema de ecuaciones
como en el ejemplo:

                        Columnas                                 3
                      ↓    ↓    ↓                             ↓  ↓  ↓
                    → 2x + 3y + 2z = 10                      [2, 3, 2  |10]  ←  
             Filas  → 4x - 3y + 4z = 20   -------------->    [4, -3,4  |20]  ←  3     (3 x 3)
                    → 5x + 4y + 5z = 30                      [5, 4, 5  |30]  ←
                                                                                


"""
menu = """

A continuacion ingresa las constantes que tienes en tu sistema de ecuaciones por ejemplo:

2x + 3y = 10  ------> [2,  3,  10]
4x - 3y = 20  ------> [4  -3   20]

"""

# Variables necesarias para los bucles

bucle = 0
opcion = 0
bucle2 = 0
bucle3 = 0

# Programa principal

while bucle == 0:
    print(Fore.WHITE + menu2)
   
    while bucle3 == 0:   # Bucle para pedir datos con manejo de errores
        
        try:
            filas = int(input(Fore.GREEN + "Ingrese el número de filas ----> "))
            columnas = int(input(Fore.RED + "Ingrese el número de columnas ----> "))
        except ValueError:
            print(Fore.RED + "¡SOLO PUEDES INGRESAR NUMEROS!, VUELVE A INTENTARLO...")
            continue
        
        if(filas != 0 and columnas != 0):
            break

    
    print(Fore.LIGHTGREEN_EX + menu)


    # La Matriz se llena de ceros para luego reeplazarlos por los datos que se ingresan

    matriz = np.zeros((filas, columnas+1))

    # Se ingresan los datos al array bidimensional con manejo de errores

    while bucle3 == 0:
        try:
            for i in range(filas):
                for j in range(columnas):
                    elemento = float(input(f"{Fore.WHITE}Ingresa el elemento en la fila {i+1}, columna {j+1}: "))
                    matriz[i][j] = elemento
                elemento = float(input(f"Ingresa el resultado en la fila {i+1}: "))
                matriz[i][columnas] = elemento
        except ValueError:
            print(Fore.RED + "¡SOLO PUEDES INGRESAR NUMEROS!, VUELVE A INTENTARLO...")
            i = 0
            j = 0
            continue
        else:
            break


    # Imprimir la matriz original

    print(Fore.LIGHTCYAN_EX + "\nMatriz original:\n")
    print(matriz)
    print("\n")


    # Método de Gauss-Jordan

    for columna_actual in range(columnas):
        
        if(filas != columnas):
            print(Fore.RED + "¡SOLO PUEDES INGRESAR MATRICES CUADRADAS (n x n)\n")
            break

        # Imprimir la matriz

        print(f"//////////////////////////////////////////////////// Matriz en la vuelta {columna_actual+1} ////////////////////////////////////////////////////")
        print("\n")

    

            # Hacer unos en la diagonal

        divisor = matriz[columna_actual][columna_actual]
        for j in range(columnas + 1):
            matriz[columna_actual][j] /= divisor  # se divide por toda la fila

        print(matriz)   # Procedimiento
        print("\n")


            # ceros debajo del uno

        for i in range(columna_actual + 1, filas):
            factor =- matriz[i][columna_actual] / matriz[columna_actual][columna_actual]  # se obtiene el numero a multiplicar
            for j in range(columnas + 1):
                if columna_actual == j:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] += factor * matriz[columna_actual][j]

        print(matriz)   # Procedimiento
        print("\n")



        # ceros encima del uno

        for i in range(columna_actual):
            factor =- matriz[i][columna_actual] / matriz[columna_actual][columna_actual]  # obtenemos el numero a multiplicar
            for j in range(columnas + 1):
                if columna_actual == j:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] += factor * matriz[columna_actual][j]


        if (columna_actual == columnas-1):
            MatrizEnCasoDeError = matriz



        print(matriz)   # Procedimiento
        print("\n")


    
    print(Fore.YELLOW + "\n -------------------------------------------------------------------------")

    try:

        print(Fore.LIGHTYELLOW_EX + "\nMatriz resuelta:\n")
        for fila in matriz:
            for elemento in fila:
                if isinstance(elemento, float):
                    print(Fraction(elemento).limit_denominator(), end=" | ")
                else:
                    print(elemento, end=" ")
            print()

    except ValueError:

        print(Back.RED + "\n" + Fore.WHITE + "La matriz no tiene solucion o tiene infinitas soluciones" + Back.RESET + "\n")
        print(MatrizEnCasoDeError)

    finally:

        print(Fore.YELLOW + "\n -------------------------------------------------------------------------\n")
    

    # Se pide confirmacion si se quiere terminar el programa


    while bucle2 == 0:
        try:
            opcion = int(input(Fore.LIGHTBLUE_EX + "¿Quieres sacar otra Matriz? (0 si / 1 no)----> "))
        except ValueError:
            print(Fore.RED + "¡Solo puedes ingresar numeros!, intentalo nuevamente...")
            continue
        
        if(opcion == 1):
            bucle = 1
            break
        else:
            clear() # Se limpia la consola y vuelve a pedir los datos para una nueva matriz
            break
        
print(Fore.LIGHTGREEN_EX + "\n" + copy + Fore.WHITE)