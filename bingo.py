import random

def generar_listado():
	listado = range(1,91)
	#random.shuffle(listado)
	return listado

def menu():
	print '\n ########## Menu principal ############ \n'
	print '1 - Generar numeros'
	print '2 - Extraer numero\n'
	print '3 - Mostrar numeros extraidos'
	print '4 - Mostrar numeros disponibles \n'
	print '5 - Comprobar numeros\n'
	print '0 - Salir \n'

def extraer_numero(numeros_disponibles, numeros_extraidos):
	numero_extraido = random.choice(numeros_disponibles)
	numeros_disponibles.remove(numero_extraido)
	numeros_extraidos.append(numero_extraido)

	print '\n ---------------------------- El numero extraido es ' + str(numero_extraido) + '\n'

	return [numeros_disponibles, numeros_extraidos]

def comprobar_numeros(numeros_extraidos):
	co = raw_input('Introduzca la combinacion a comprobar: ')
	comprobar = co.split()

	comprobacion_correcta = 1
	for numero in comprobar:
		print 'Comprobamos ' + str(numero)
		if numeros_extraidos.count(int(numero)) == 0:
			comprobacion_correcta = 0
	if comprobacion_correcta == 0:
		print '---------------------------- La comprobacion NO ES CORRECTA'
	else:
		print '---------------------------- La comprobacion ES CORRECTA'


######## Main function ########

print 'Bingo vermucico 2020 \n'

numeros_disponibles = generar_listado()
numeros_extraidos = []

opcion_seleccionada = 99

while opcion_seleccionada != 0:

	menu()

	try:
	    opcion_seleccionada=int(raw_input('\n##### Seleccione una opcion: '))
	except ValueError:
	    print "La opcion no es un numero"

	if opcion_seleccionada == 1:
		numeros_disponibles = generar_listado()
		numeros_extraidos = []
	elif opcion_seleccionada == 2:
		output = extraer_numero(numeros_disponibles, numeros_extraidos)
		numeros_disponibles = output[0]
		numeros_extraidos = output[1]
	elif opcion_seleccionada == 3:
		numeros_extraidos.sort()
		print '---------------------------- Los numeros extraidos son ' + str(numeros_extraidos)
	elif opcion_seleccionada == 4:
		print '---------------------------- Los numeros disponibles son ' + str(numeros_disponibles)
	elif opcion_seleccionada == 5:
		comprobar_numeros(numeros_extraidos)
	else:
		print '\n #########  Fin del Bingo #########'
