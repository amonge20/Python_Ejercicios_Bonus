# Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
# nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
# David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
# introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
# imprimir la nota media de los alumnos junto con el DNI.
# Supón ahora que tu input es un string como este:
# ‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
# Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
# Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
# Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
# de todos los alumnos en ese string. 

# Variable de la cadena que convertiremos en Lista
matrizCadena = "David Fernandez,12311267A,43527,2,9.1,7.6,2.4\nMaria Garcia,12316487A,43527,2,7.1,8.6,5.4\nJuan Perez,647829236A,43527,2,8.1,8.5,8.4\n"

# Convertir de cadena a lista
matriz = [fila.split(",") for fila in matrizCadena.strip().split("\n")]
print(matriz)

# Una vez que tengamos la lista convertida, recorremos el bucle para mostrar la nota media y el DNI de los alumnos
print("---- NOTA FINAL DE CADA ALUMNO SEGUN SU DNI ----")

# Recorremos un bucle para filtrar los datos
for alumno in matriz:
     # Filtramos el DNI y la nota media para despues calcular la nota final
     dni = alumno[1]
     notas = [float(n) for n in alumno[4:]]    # Convertir a float
     media = sum(notas) / len(notas)

     # Resultado
     print(f"DNI:{dni}. Nota Final:{round(media,2)}")