# Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
# ese caso imprima dos listas correspondientes a:
# 1. La fila cuyos elementos suman el máximo
# 2. La columna cuyos elementos suman el máximo
# Si no se trata de una matriz devolverá dos listas vacías.
# Por ejemplo:
# M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
# M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
# (Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
# numero de objetos) 

# Creacion de las listas de las matrices
Matriz = [[[2,5,3],[6,1,8],[7,5,4]],  # Matriz 1
        [[4,2,3],[4,5],[6,8,2]]     # Matriz 2
        ]

# Recorremos un bucle para la lista de matrices
for M in Matriz:
    # Inicializar las variables
    L1 = []
    L2 = []
    # Variable para la matriz booleana
    esMatriz = True
    
    # Verificacion de la matriz
    if len(M) == 0:
        esMatriz = False
    else:
        longitud = len(M[0])
        for fila in M:
            if len(fila) != longitud:
                esMatriz = False
                break

    # Si es matriz, calcularemos filas y columnas de las 2 matrices
    if esMatriz:
        # Suma maxima de las filas
        sumaFilas = [sum(fila) for fila in M]
        indFilaMax = sumaFilas.index(max(sumaFilas))
        L1 = M[indFilaMax]

        # Suma maxima de las columnas
        numeroFilas = len(M)
        numeroColumnas = len(M[0])
        columnas = []

        # Recorriendo el bucle para las columnas
        for c in range(numeroColumnas):
            columna = [M[f][c] for f in range(numeroFilas)]
            columnas.append(columna)

        sumaColumnas = [sum(col) for col in columnas]
        indColMax = sumaColumnas.index(max(sumaColumnas))
        L2 = columnas[indColMax]
        
    # Resultado
    print("Matriz:",M)
    print("L1 = ",L1)
    print("L2 = ",L2)