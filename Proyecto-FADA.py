import sys
import time

def Recibir_Archivo():
    #archivo = input("Ingrese la direccion del archivo: ")
    Recibir_Entrada("entrada-fada.txt")


def Recibir_Entrada(archivo):

    archivo_entrada = open(archivo, "r") # se abre el archivo para leerlo, una vez que lo lee lo cierra

    NK = archivo_entrada.readline().split() #Separa la primera linea del resto del arreglo ya que esta sera nuestro K Y N
    NK = list(map(int, NK)) #pasamos a entero el arreglo

    trabajadores = archivo_entrada.read().splitlines() #Se almacena los trabajadores del arreglo
    trabajadores = list(map(int, trabajadores)) #pasamos a entero el arreglo

    archivo_entrada.close() #Cerramos el archivo
    
    Verificar_Entrada(NK, trabajadores)

    return NK, trabajadores


def Verificar_Entrada(NK, trabajadores):

    if NK[0] == len(trabajadores) and (NK[0] > 0) and (len(trabajadores) > 0) and(NK[1]>1):
        creacion_grupos(NK, trabajadores)

    else:
        sys.exit("EL NUMERO DE TRABAJADORES NO COINCIDEN O NO HAY TRABAJADORES PARA FORMAR GRUPOS, POR FAVOR VERIFIQUE LA INFORMACION SUMINISTRADA")


def mejor_trabajador(grupo): # Devuelve el índice del mejor trabajador
    mejor = max(grupo)
    index = grupo.index(mejor)
    return index

#Crea los pares del grupo
def creacion_grupos(NK,trabajadores):
    grupos = []
    solucion = []
    # O(techo(N/K)-> maximo de grupos que se pueden formar )
    for i in range(0, NK[0], NK[1]): # separa el arreglo "trabajadores" en suplistas de maximo "K" elementos
        grupos.append(trabajadores[i:i+NK[1]])
    
    for i in range(len(grupos) -2, -1,-1): #O(techo(N/K))
        if grupos[i][mejor_trabajador(grupos[i])] < grupos[i+1][mejor_trabajador(grupos[i+1])]: # se compara que el elemento mayor de un grupo sea menor a el elemento mayor del siguiente grupo
            if len(grupos[i+1]) < NK[1]: # se verifica que el siguiente grupo puede tener mas elementos en su grupo
                j = NK[1] - len(grupos[i+1]) # maximo de elementos que se pueden añadir
                # en el peor caso se ejecuta K veces, es decir, se deja solo un elemento en el grupo
                while j > 0: # añade los elementos posibles al siguiente grupo y a la vez los borra del grupo en el que estaba
                    grupos[i+1].insert(0, grupos[i].pop()) # añade los elemento que puedan entrar al grupo
                    j -= 1
    
    i = 0
    inicio = 0
    # O(techo(N/K))
    while i < len(grupos): # llena el arreglo solucion con las tuplas que indica el trabajador con el que inicia y termina cada grupo
        solucion.append([inicio + 1 , inicio + len(grupos[i])])
        inicio += len(grupos[i])
        i +=1
    Generar_Salida(solucion)


def Generar_Salida(pares):

    with open("salida-fada.txt", "w") as archivo_salida: #se crea un archivo el cual se puede escribir 
        for e in pares:                             #Recorre cada elemento del arreglo 
            archivo_salida.write(str(e[0]) + " " + str(e[1]) + "\n")  #ingresa en el archivo salida cada parte del arreglo con un salto de linea con su respectivo formato


Recibir_Archivo()

