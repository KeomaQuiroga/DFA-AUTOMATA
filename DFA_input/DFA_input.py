def escribirArchivo(nombreArchivo, contenido):  #Crea un archivo de resultado si ve que no existe uno
    with open(nombreArchivo, 'a') as archivo:
            archivo.write(contenido)

#variables
estados = []    #cantidad de estados del DFA
estadoInicial = ' '
estadosFinales = []
sigma = []  #lenguaje
transiciones = []

archivo = open("dfa.txt", "w")
#INPUT USUARIO
#definir estados
print("SIMULADOR DFA")
print("Alfabeto por defecto: 0 1")
print("Siga las instrucciones \n")
numEstados = int(input("Ingrese el numero de estados de su DFA: "))
for i in range(0, numEstados):
    if (i == numEstados):
        break
    else:
        archivo.write(f"q{i},")

#definir estado inicial
num = ""
inicio = input("Ingrese su estado inicial con el formato qx: ")
for car in inicio:
    if car.isnumeric():
        num += car
if int(num) > numEstados:
    archivo.write("\nError")
    quit()
else:
    inicio = num
    archivo.write(f"\nq{inicio}\n")

#definir estados finales
print("Ingrese un estado final de la forma qx. Si desea ingresar otro presione enter, si desea acabar escriba salir.")
while(True):
    num = ""
    estado = input("Estado: ")

    if estado.lower() == "salir" and len(estadosFinales) >= 1:
        break
    elif estado.lower() != "salir":
        for car in estado:
            if car.isnumeric():
                num += car
        estado = num
        if estado.isdigit:
            estadosFinales.append(estado)
            archivo.write(f"q{estado},")
        else:
            print("Formato no valido")
    else:
        print("Necesita minimo un estado final")

#definir lenguaje
languaje = "0, 1"
archivo.write(f"\n{languaje}")

#definir transiciones
print("Ingrese las transiciones de la forma qx qy:")
num = 0
while num < numEstados: #transicion por cada estado
    transicion = input(f"Estado q{num}: ")
    archivo.write(f"\n{transicion}")
    num+=1
archivo.close()

#pruebas
archivo = open("pruebas.txt", "w")

pruebas = []
print("Ingrese strings, escriba salir para salir")
while True:
    entrada = input("Ingrese un string: ")
    if entrada.lower() == "salir" and len(pruebas) >= 1:
        break
    else:
        pruebas.append(entrada)
        archivo.write(entrada + "\n")

archivo.close()

#APLICACION DFA
archivo = open("dfa1.txt")

i = 0
#lee cada linea
for linea in archivo.readlines():
    i+=1
    #lee cada caracter
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
    if str(estFinal) in estadosFinales:
        escribirArchivo("resultado.txt", "true\n")
    else:
        escribirArchivo("resultado.txt", "false\n")

archivo.close()
resultado.close()