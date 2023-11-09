#Define los archivos de texto para trabajar
archivo_entrada = "data\calificaciones.txt"
archivo_salida = "data\promedios.txt"

#Abre el archivo de entrada y salida
with open(archivo_entrada,"r",encoding="utf8") as f, open (archivo_salida,"w",encoding="utf8") as h:
    #Separa el nombre de las calificaciones en si
    for line in f:
        partes = line.split()
        apellido = partes[1].upper()
        nombre = partes[0]
        calis = [int(calif) for calif in partes[2:]]
        
        #Calcula la calificacion promedio para la persona
        promedio = (sum(calis)/len(calis))

        #Escribe el resultado en el nuevo archivo
        h.write(f"{apellido}, {nombre}: {round(promedio,2)}\n")
