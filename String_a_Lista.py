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

# Creamos una lista de los alumnos con sus datos
# nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3
Lista_alumnos = [
    ['David Fernandez', '12311267A', 43527, 2, 9.1, 7.6, 2.4],
    ['Maria Garcia', '12316487A', 43527, 2, 7.1, 8.6, 5.4],
    ['Juan Perez', '647829236A', 43527, 2, 8.1, 8.5, 8.4]
    ]

# Lista vacia para la nota final de los alumnos
NotaFinal = []

print("---- NOTA FINAL DE CADA ALUMNO SEGUN SU DNI ----")

# Bucle para recopilar la nota final junto con su DNI
for alumno in Lista_alumnos:
    # Filtramos el DNI y la nota media para despues calcular la nota final
    dni = alumno[1]
    notaMedia = alumno[4:]
    media = sum(notaMedia) / len(notaMedia)
    # Se añade en la lista de "Nota final"
    NotaFinal.append(media)
    # Resultado
    print(f"DNI:{dni}. Nota Final:{round(media,2)}")