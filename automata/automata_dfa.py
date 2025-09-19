def escribirArchivo(nombreArchivo, contenido):  #Crea un archivo de resultado si ve que no existe uno
    with open(nombreArchivo, 'a') as archivo:
            archivo.write(contenido)


#Define al DFA
estados = []
estadoInicial = ' '
estadosFinales = []
sigma = []
transiciones = []

archivo = open("dfa1.txt")

i = 0
for linea in archivo.readlines():
    i+=1
    for car in linea:
        if car.isnumeric():
            if i == 1:  #esatados
               estados.append(car)
            elif i == 2:    #estado inicial
                estadoInicial = car
            elif i == 3:    #estados finales
                  estadosFinales.append(car)
            elif i == 4:    #sigma
                sigma.append(car)
            else:   #transiciones
                transiciones.append(car)

archivo.close()

i = 0
num = 0
DFA = {}
while num < len(estados):   #Define el DFA
    DFA[num] = transiciones[i], transiciones[i+1]
    i+=2
    num+=1

print(DFA)

#Lee las pruebas y escribe resultados
archivo = open("pruebas.txt")
resultado = open("resultado.txt", "w")
estFinal = 0

for linea in archivo:
    i = 0
    num+=1
    estFinal = 0
    for car in linea:
        i = estFinal
        if car == str(sigma[0]):
            estFinal = int(DFA[i][0])
        else:
            estFinal = int(DFA[i][1]) 

    #chequea si es correcto     
    if str(estFinal) in estadosFinales:
        escribirArchivo("resultado.txt", "true\n")
    else:
        escribirArchivo("resultado.txt", "false\n")

archivo.close()
resultado.close()