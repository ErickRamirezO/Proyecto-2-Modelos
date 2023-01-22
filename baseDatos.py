from replit import Database
from memory_profiler import profile
import big_o, main
import datos as Datos
from os import system
import matplotlib.pyplot as graficas

db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzQ0NjY0MDYsImlhdCI6MTY3NDM1NDgwNiwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.CKcTKIU9y90DWPlsoAK1dAaX5sL4RcqLxU9TdgDhErquYi_j7R_i4aviCtUAEi3WHibUbEhXw123MLi25_q2Hw")


def cargarDBLibros():
	"""
 Funcion: carga una base de datos de libros. Primero, imprime un mensaje indicando que se está cargando la base de datos. Luego, asigna un 
          arreglo vacío a cada una de las categorías de la base de datos.

 Parametros: Ninguno 

 Retorna: no retorna nada 
 
 	"""
  #mensaje de que se esta cargando la base de datos de los libros 
	print("\033[0mCargando base de datos libros...")
  # Copias disponibles, Ubicación y Conservación).
	db["Titulos_libros"] = db["Autores_libros"] = db["Disponibilidad"] = db[
	 "Copias_disponibles"] = db["Ubicacion"] = db["Conservacion"] = []
  #agrega los datos correspondientes a cada una de las categorías a partir de los datos contenidos en las listas del archivo datos.py
	for i in range(len(Datos.titulos)):
    #datos contenidos de cada clase 
		db["Titulos_libros"].append(Datos.titulos[i])
    #datos contenidos de cada clase 
		db["Autores_libros"].append(Datos.autores[i])
    #datos contenidos de cada clase 
		db["Disponibilidad"].append(Datos.disponibilidad[i])
    #datos contenidos de cada clase 
		db["Copias_disponibles"].append(Datos.copias_disponibles[i])
    #datos contenidos de cada clase 
		db["Ubicacion"].append(Datos.ubicacion[i])
    #datos contenidos de cada clase 
		db["Conservacion"].append(Datos.conservacion[i])
  #Finalmente, imprime un mensaje indicando que los libros se han cargado exitosamente.
	print("\033[32mLibros cargados exitosamente")


def cargarDBEstudiantes():
	"""
 Funcion: carga una base de datos de estudiantes. Primero, imprime un mensaje indicando que se está cargando la base de datos de estudiantes. 
          Luego, asigna un arreglo vacío a cada una de las categorías de la base de datos

 Parametros: No contiene ningun parametro 

 Retorna: No retorna nada 
	"""
  # mensaje de que se esta cargando la base de datos de los estudiantes 
	print("\033[0mCargando base de datos de estudiantes...")
	#lista estudiantes
	db["Estudiantes"] = db["Carrera_estudiantes"] = db[
	 "Numero_libros_reservados"] = db["Numero_libros_prestados"] = db[
	  "Numero_Visitas_Estudiante"] = db["Notificacion_devolucion"] =db["Numero_multas"]=db["Prestamo_activo"]= db["Registro_devolucion"]=[]
  #agrega los datos correspondientes a cada una de las categorías a partir de los datos contenidos en una clase llamada "Datos"
	for i in range(len(Datos.estudiantes)):
    #datos correspondientes a cada una de las categorías
		db["Estudiantes"].append(Datos.estudiantes[i])
     #datos correspondientes a cada una de las categorías
		db["Carrera_estudiantes"].append(Datos.carrera[i])
     #datos correspondientes a cada una de las categorías
		db["Numero_libros_reservados"].append(Datos.numero_libros_reservados[i])
     #datos correspondientes a cada una de las categorías
		db["Numero_libros_prestados"].append(Datos.numero_libros_prestados[i])
     #datos correspondientes a cada una de las categorías
		db["Numero_Visitas_Estudiante"].append(Datos.numero_visitas_estudiante[i])
     #datos correspondientes a cada una de las categorías
		db["Notificacion_devolucion"].append(Datos.notificacion_devolucion[i])
     #datos correspondientes a cada una de las categorías
		db["Numero_multas"].append(Datos.numero_multas[i])
	 #datos correspondientes a cada una de las categorías
		db["Prestamo_activo"].append(Datos.prestamo_activo[i])
	  #datos correspondientes a cada una de las categorías
  #Finalmente, imprime un mensaje indicando que los estudiantes se han cargado exitosamente.
	print("\033[32mEstudiantes cargados exitosamente")

def cargarSalas():
	"""
 Funcion: carga una base de datos de salas de estudio. Primero, imprime un mensaje indicando que se está cargando las salas. Luego, asigna un 
        arreglo vacío a cada una de las categorías de la base de datos (Salas de estudio, Sala disponible y Sala reservada)

 Parametros: No contiene ninguna funcion 

 Retorna: No retorna ningun dato 
 	"""
  #mensaje de que esta cargando las salas 
	print("\033[0mCargando salas...")
	#lista con las categorias salas de estudio, sala disponible y sala reservada
	db["Salas_de_estudio"] = db["Sala_disponible"]= db["Sala_reservada"]=[]
  #  En un ciclo "for", agrega los datos correspondientes a cada una de las categorías a partir de los datos contenidos en una clase llamada "Datos"
	for i in range(len(Datos.salas)):
    #los datos correspondientes a cada una de las categorías
		db["Salas_de_estudio"].append(Datos.salas[i])
    #los datos correspondientes a cada una de las categorías
		db["Sala_disponible"].append(Datos.sala_disponible[i])
    #los datos correspondientes a cada una de las categorías
		db["Sala_reservada"].append(Datos.sala_reservada[i])

def cargarPersonal():
	"""
 Funcion: carga una base de datos del personal de la bibliotca. Primero, imprime un mensaje indicando que se está cargando las salas. Luego, asigna un arreglo vacío a cada una de las categorías de la base de datos (Salas de estudio, Sala disponible y Sala reservada)

 Parametros: No contiene ninguna funcion 

 Retorna: No retorna ningun dato 
 	"""
  #mensaje de que esta cargando el personal de biblioteca 
	print("\033[0mCargando personal de biblioteca...")
	#lista con las categorias salas de estudio, sala disponible y sala reservada
	db["Personal"] = db["Salarios"]= db["Cargo"]= db["Jornada_laboral"]=db["Horas_trabajas"]=[]
  #  En un ciclo "for", agrega los datos correspondientes a cada una de las categorías a partir de los datos contenidos en una clase llamada "Datos"
	for i in range(len(Datos.personal)):
    #los datos correspondientes a cada una de las categorías
		db["Personal"].append(Datos.personal[i])
    #los datos correspondientes a cada una de las categorías
		db["Salarios"].append(Datos.salarios[i])
    #los datos correspondientes a cada una de las categorías
		db["Cargo"].append(Datos.cargo[i])
	#los datos correspondientes a cada una de las categorías
		db["Jornada_laboral"].append(Datos.jornada_laboral[i])
	#los datos correspondientes a cada una de las categorías
		db["Horas_trabajas"].append(Datos.horas_trabajas[i])

#extra
def listadoEstudiantes():
	""" 
 Funcion: La funcion imprime la lista de estudiantes que se han ingresado en la base de datos. 

 Parametro:No contiene parametros 

 Retorna: No retorna ningun dato 
 
 	"""
  #Primero, imprime un título "Estudiantes ingresados"
	print("Estudiantes ingresados")
	print("----------------------")
  #Luego, utiliza el método "format()" para dar formato a los encabezados de cada columna ("Número", "Estudiante" y "Carrera") para que se impriman en la consola
	print("\033[0m{:^8}\033[33m{:^20}\033[32m{:^25}".format(
	 "Número", "Estudiante", "Carrera"))
  #En un ciclo "for", se imprime el número (i + 1), el nombre del estudiante y la carrera del estudiante correspondiente, tomando estos datos de la base de datos. 
	for i in range(len(db["Estudiantes"])):
    #El formato de la impresión es con color, con los encabezados de las columnas en color diferente.
		print("\033[0m{:^8}{:^20}{:^25}".format(i + 1, db["Estudiantes"][i],
		                                        db["Carrera_estudiantes"][i]))


#extra punto numero 5
def listadoEstudiantesReserva():
	"""
 Funcion: La funcion imprime una lista de estudiantes con los libros que han reservado.

 Parametros: No, contiene ningun parametro

 Retorna: No, retorna ningun dato
 	"""
  #Primero, imprime un título "Estudiantes ingresados"
	print("Estudiantes ingresados")
  # línea de separación.
	print("----------------------")
  #imprime una nota indicando que los estudiantes que tienen libros reservados aparecerán marcados en verde
	print(
	 "Los estudiantes que tienen reservados libros se marcan de color \033[32mverde"
	)
  #Utiliza el método "format()" para dar formato a los encabezados de cada columna ("Número", "Estudiante", "Carrera" y "Libros reservados") para que se impriman en la consola.
	print("\033[0m{:^8}\033[33m{:^20}\033[35m{:^25}\033[31m{:^25}".format(
	 "Número", "Estudiante", "Carrera", "Libros reservados"))
  #En un ciclo "for", se recorre la base de datos y se imprime el número (i + 1), el nombre del estudiante, la carrera del estudiante correspondiente.
	for i in range(len(db["Estudiantes"])):
    #número de libros reservados, tomando estos datos de la base de datos.
		if db["Numero_libros_reservados"][i] > 0:
			print("\033[32m{:^8}{:^20}{:^25}{:^25}".format(
			 i + 1, db["Estudiantes"][i], db["Carrera_estudiantes"][i],
			 db["Numero_libros_reservados"][i]))
    #Si el número de libros reservados es mayor a cero, se imprime el registro en verde, de lo contrario, se imprime en blanco
		else:
			print("\033[0m{:^8}{:^20}{:^25}{:^25}".format(
			 i + 1, db["Estudiantes"][i], db["Carrera_estudiantes"][i],
			 db["Numero_libros_reservados"][i]))


def registro_estudiante(lista):
	"""
 Funcion: La funcion se encarga de registrar un nuevo estudiante en la base de datos.

 Parametros: nombre, carrera

 Retorna: Retorna un mensaje 
 	"""
	nombre = lista[0]
	carrera = lista[1]
  #Primero, utiliza un ciclo "for" para recorrer la lista de estudiantes existentes en la base de datos. 
	for i in range(len(db["Estudiantes"])):
    #Utiliza el método "in" para verificar si el nombre del estudiante ingresado ya existe en la lista.
		if str(nombre) == db["Estudiantes"][i]:
      #mensaje de ingreso del nombre ya existio 
			return "\033[31mEl nombre ingresado ya existe"
	
  #Si el nombre no existe, agrega el nombre del estudiante, la carrera, el número de libros reservados y el número de visitas a la base de datos. 
			# Agregar el nuevo estudiante a la base de datos de replit
	db["Estudiantes"].append(nombre)
	db["Carrera_estudiantes"].append(carrera)
	db["Numero_libros_reservados"].append(0)
	db["Numero_Visitas_Estudiante"].append(0)
	    #Finalmente, imprime un mensaje indicando que el estudiante ha sido registrado exitosamente.
	return '\033[32mEstudiante registrado exitosamente'

def obtenerLibros():
	"""
  Funcion: La funcion imprime una lista de libros disponibles en la biblioteca

 Parametros:No, contiene ningun parametro

 Retorna: No, retorna ningun valor ni dato
 	"""
  #Utiliza el método "format()" para dar formato a los encabezados de cada columna ("Número", "Libros", "Autor" y "Disponibilidad") para que se impriman en la consola
	print("\033[0m{:^8}\033[33m{:^40}\033[36m{:^28}\033[32m{:^14}".format(
	 "Número", "Libros", "Autor", "Disponibilidad"))
  #En un ciclo "for", se recorre la base de datos y se imprime el número (i + 1), el nombre del libro, el autor y la disponibilidad del libro correspondiente, tomando estos datos de la base de datos
	for i in range(len(db["Titulos_libros"])):
    #El formato de la impresión es con color.
		print("\033[0m{:^8}{:^40}{:^28}{:^14}".format(i + 1, db["Titulos_libros"][i],
		                                              db["Autores_libros"][i],
		                                              db["Disponibilidad"][i]))



def validarEjemplarDisponible(i):
	"""
  Funcion: La funcion valida si un ejemplar de un libro especificado por el parámetro "i" está disponible

 Parametros: i

 Retorna: retorna true o false
 	"""
  # Verifica si el valor de la disponibilidad del libro en la posición "i" de la base de datos es "Si". 
	if db["Disponibilidad"][i] == "Si":
    #Si es así, devuelve "True
		return True
  #de lo contrario devuelve "False". Esta función es utilizada para determinar si un libro específico está disponible para ser prestado o no.
	return False


def verificarEstudiante(nombre_estudiante):
	"""
  Funcion: La funcion valida si un estudiante especificado por el parámetro "nombre_estudiante" existe en la base de datos.

 Parametros: nombre_estudiante

 Retorna: true o false 
 	"""
  #Utiliza un ciclo "for" para recorrer la lista de estudiantes existentes en la base de datos
	for i in range(len(db["Estudiantes"])):
    #Verifica si el nombre del estudiante en la posición "i" de la base de datos es igual al nombre del estudiante especificado en el parámetro, convirtiendo el nombre del estudiante en la base de datos en minúsculas con el método "lower()". 
		if db["Estudiantes"][i].lower() == nombre_estudiante:
      #Si el nombre del estudiante coincide Si el nombre del estudiante coincide
			return True
  #de lo contrario devuelve "False"
	return False


def validarNumeroReservaLibros(nombre_estudiante):
	"""
  Funcion: La funcion obtiene el número de libros reservados por un estudiante específico

 Parametros: nombre_estudiante

 Retorna Numero_libros_reservados
 	"""
  #Utiliza un ciclo "for" para recorrer la lista de estudiantes existentes en la base de datos.
	for i in range(len(db["Estudiantes"])):
    #erifica si el nombre del estudiante en la posición "i" de la base de datos es igual al nombre del estudiante especificado en el parámetro, convirtiendo el nombre del estudiante en la base de datos en minúsculas con el método "lower()"
		if db["Estudiantes"][i].lower() == nombre_estudiante:
      #Si el nombre del estudiante coincide, devuelve el número de libros reservados del estudiante correspondiente.
			return db["Numero_libros_reservados"][i]


def actualizarLibrosReservados(lista):
	"""
  Funcion: La funcion actualiza la base de datos de acuerdo a la acción de reservar o prestar un libro.

 Parametros: nombre_estudiante, numeroLibroReservar,reserva_o_prestamo

 Retorna: No, retorna ningun dato o valor 
 	"""
	nombre_estudiante = lista[0]
	numeroLibroReservar = lista[1]
	reserva_o_prestamo = lista[2]
  #divide el nombre del estudiante en dos partes, el primer y segundo nombre.
	nombre = nombre_estudiante.split()
  #crean listas vacías en la base de datos para almacenar los libros reservados y prestados por el estudiante
	db["Libros_reservados_" + nombre[0] + "_" +
	   nombre[1]] = db["Libros_prestados_" + nombre[0] + "_" + nombre[1]] = []
  #Utiliza un ciclo "for" para recorrer la lista de estudiantes existentes en la base de datos. Verifica si el nombre del estudiante en la posición "i" de la base de datos es igual al nombre del estudiante especificado en el parámetro
	for i in range(len(db["Estudiantes"])):
    #onvirtiendo el nombre del estudiante en la base de datos en minúsculas con el método "lower()".
		if db["Estudiantes"][i].lower() == nombre_estudiante:
			#1 para reserva y 2 para prestamo
			if reserva_o_prestamo == 1:
        #Si el nombre del estudiante coincide, se utiliza el parámetro "reserva_o_prestamo" para determinar si se debe actualizar la cantidad de libros reservados o prestados.
				db["Numero_libros_reservados"][i] = db["Numero_libros_reservados"][i] + 1
				db["Libros_reservados_" + nombre[0] + "_" + nombre[1]].append(
				db["Titulos_libros"][numeroLibroReservar])
        #mensaje de que el ejemplejar se reservo con exito 
				return "\033[32m ¡Ejemplar reservado con éxito!"
      #En caso de ser 2, se aumenta en 1 el número de libros prestados del estudiante y se agrega el título del libro prestado a la lista de libros
			else:
				db["Numero_libros_prestados"][i] = db["Numero_libros_prestados"][i] + 1
				db["Libros_prestados_" + nombre[0] + "_" + nombre[1]].append(
				db["Titulos_libros"][numeroLibroReservar])
        #mesaje de que se va a prestar el libro 
				return "\033[32m ¡Ejemplar prestado con éxito!"


def listadoEstudiantesNotificados():
	"""
  Funcion: La funcion imprime en pantalla una lista de estudiantes que han sido notificados para devolver un libro.

 Parametros: No, contiene ningun parametro

 Retorna: No, retorna ningun valor 
 	"""
  #La primera linea imprime el encabezado de la tabla con los nombres de las columnas, utilizando el formato " {:^8} {:^20} {:^25} {:^60} " para alinear los datos en el centro y darles un ancho específico.
	print("\033[32m{:^8}{:^20}{:^25}{:^60}".format("Número", "Estudiante",
	                                               "Carrera", "Notificación"))
  #Utiliza un ciclo "for" para recorrer la lista de estudiantes existentes en la base de datos. 
	for i in range(len(db["Estudiantes"])):
    #erifica si la notificación de devolución de un libro en la posición "i" de la base de datos es diferente a una cadena vacía.
		if db["Notificacion_devolucion"][i] != "":
			print("\033[32m{:^8}{:^20}{:^25}{:^60}".format(
			 i + 1, db["Estudiantes"][i], db["Carrera_estudiantes"][i],
      #Si la notificación de devolución no es vacía, se imprime en pantalla la información del estudiante, el número, el nombre, la carrera y la notificación correspondiente.
			 db["Notificacion_devolucion"][i]))


def notificarUsuario(numero_estudiante):
	"""
  Funcion: La funcion envia una notificacion al estudiante seleccionado, informando de los libros pendientes por devolver

 Parametros: numero_estudiante

 Retorna: No, retorna ningun valor 
 	"""
  #La línea comprueba si el número de libros reservados para un estudiante (especificado por la variable "número_estudiante") es mayor que cero. Si es así, se ejecutará el código en el bloque if. De lo contrario, se ejecutará el código en el otro bloque.
	if db["Numero_libros_reservados"][numero_estudiante - 1] > 0:
    #Esta línea asigna el valor del número de libros reservados para el alumno a la variable "total_libros".
		total_libros = db["Numero_libros_reservados"][numero_estudiante - 1]
    #Esta línea asigna el nombre del estudiante a la variable "nombre_estudiante".
		nombre_estudiante = db["Estudiantes"][numero_estudiante - 1]
    #Esta línea agrega una notificación al diccionario "Notificacion_devolucion" 
		db["Notificacion_devolucion"][
    #para el alumno, con el mensaje "¡Aviso! Tienes " + el número total de libros + " libros pendientes de devolución"
		 numero_estudiante - 1] = "¡Aviso! Tiene " + str(
       #Esta línea imprime un mensaje que indica que la notificación se envió con éxito al estudiante.
		  total_libros) + " libros pendientes por devolver"
		print(
		 f"\033[32m Se ha notificado satisfactoriamente al estudiante \033[0m{nombre_estudiante}"
		)
    #Este es el comienzo del bloque else, que se ejecuta si el número de libros reservados para el estudiante es cero.
	else:
    #Esta línea imprime un mensaje indicando que el estudiante no tiene ningún libro reservado, por lo que no se puede enviar una notificación.
		print("No se puede enviar la notificación al estudiante " +
		      db["Estudiantes"][numero_estudiante - 1] +
		      " porque no tiene reservado ningún libro")
    #Esta línea solicita al usuario que presione cualquier tecla para elegir a otro estudiante.
		input("Presione cualquier tecla para escoger otro estudiante")
    #Esta línea borra la pantalla del terminal.
		system("clear")
    #Esta línea imprime el título de la sección de notificaciones.
		print("---Notificaciones---")
    #Esta línea explica el código de colores utilizado en la lista de estudiantes.
		print(
		 "Los estudiantes que tienen reservados libros se marcan de color \033[32mverde"
		)
    #Esta línea llama a una función llamada "listadoEstudiantesReserva()", que presumiblemente muestra una lista de estudiantes que tienen libros reservados.
		listadoEstudiantesReserva()
    #Este bucle while se ejecuta hasta que el usuario ingresa un número entero válido como entrada.
		while True:
			try:
				numero = int(
          #Esta línea solicita al usuario que ingrese el número de un estudiante para notificar.
				 input("\nIngrese el número del estudiante para notificarle: "))
				break
        #Esta línea intenta convertir la entrada en un número entero. Si no es posible convertir la entrada a un número entero, generará un ValueError.
			except ValueError:
        #Si el bloque try genera un ValueError, el código de este bloque except se ejecuta, imprime un mensaje de error y borra la pantalla.
				print("Por favor, ingrese solo números.")
        #Esta línea borra la pantalla del terminal.
				system("clear")
        #Esta línea llama a la función "notificarUsuario()" con el número del estudiante a notificar como parámetro.
		notificarUsuario(numero)


def seguimientoLibros():
	"""
  Funcion: imprime los encabezados de diferentes campos de los libros

 Parametros: No, contiene parametros

 Retorna: No, retorna ningun dato 
 	"""
  #Esta línea imprime una cadena con los encabezados de diferentes campos de libros, como "Libros", "Autor", "Disponibilidad", "Número de copias", "Ubicación", "Almacenamiento", y utiliza el formato de alineación central.
	print("\033[33m{:^40}{:^28}{:^14}{:^18}{:^40}{:^14}".format(
	 "Libros", "Autor", "Disponibilidad", "Número de copias", "Ubicacion",
	 "Conservación"))
  #Esta línea inicia un ciclo for que iterará a través del rango de longitud del campo "Titulos_libros" en el diccionario "db".
	for i in range(len(db["Titulos_libros"])):
    #Esta línea imprime el título, el autor, la disponibilidad, el número de copias, la ubicación y el estado de cada libro en el diccionario "db", utilizando el formato de alineación central.
		print("\033[0m{:^40}{:^28}{:^14}{:^18}{:^40}{:^9}".format(
		 db["Titulos_libros"][i], db["Autores_libros"][i], db["Disponibilidad"][i],
      #Esta línea usa el índice del bucle for para acceder a la condición del libro actual en el diccionario "db".
		 db["Copias_disponibles"][i], db["Ubicacion"][i], db["Conservacion"][i]))


def validarbusquedaLibro(libro):
	"""
  Funcion: La funcion que toma un parámetro "libro" y retorna un valor booleano (verdadero o falso).

 Parametros:libro

 Retorna: nos retorna un verdadero si se cumple la condicion y un falso si es no se llega a cumplir 
 	"""
  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Titulos_libros" en el diccionario "db".
	for i in range(len(db["Titulos_libros"])):
    #Esta línea verifica si el título del libro actual en el índice del bucle es igual al parámetro "libro" o si el autor del libro actual en el índice del bucle es igual al parámetro "libro", en ambos casos se convierten a minúsculas. 
		if db["Titulos_libros"][i].lower() == libro or db["Autores_libros"][i].lower(
		) == libro:
      #Si se cumple alguna de estas condiciones, se retorna verdadero.
			return True
  #Esta línea se ejecuta si el bucle termina sin encontrar una coincidencia, se retorna falso.
	return False


def buscarLibro(libro):
	"""
  Funcion: La funcion busca en la base de datos "db" si existe un libro con un título o un autor que coincida con el parámetro "libro" (tanto el título como el autor se comparan en minúsculas) y si se encuentra una coincidencia, imprime el título, el autor y el estado de disponibilidad del libro encontrado.

 Parametros: libro

 Retorna: No, retorna ningun dato 
 	"""
  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Titulos_libros" en el diccionario "db".
	for i in range(len(db["Titulos_libros"])):
    #Esta línea verifica si el título del libro actual en el índice del bucle es igual al parámetro "libro" o si el autor del libro actual en el índice del bucle es igual al parámetro "libro", en ambos casos se convierten a minúsculas. Si se cumple alguna de estas condiciones, se ejecuta el código dentro del if.
		if db["Titulos_libros"][i].lower() == libro or db["Autores_libros"][i].lower(
		) == libro:
      #Esta línea imprime un mensaje indicando que se ha encontrado un libro con el título o el autor que coincide con el parámetro "libro", y detalla el título y el autor del libro encontrado.
			print(
			 f"""\n\033[0m Se encontró el siguiente libro\n\n\033[33m{db["Titulos_libros"][i]} de {db["Autores_libros"][i]}"""
			)
      #Esta línea imprime el estado de disponibilidad del libro encontrado en el diccionario "db"
			print(f"""\033[0mDisponible: \033[36m{db["Disponibilidad"][i]}""")


#punto 7
def actualizarUsuario():
	"""
  Funcion: La función llamada "actualizarUsuario()" que no tiene ningún parámetro y no retorna ningún valor.

 Parametros: No, contiene parametros

 Retorna: no, retorna ningun dato 
 	"""
  #Esta línea llama a una función llamada "listadoEstudiantes()" que probablemente imprime una lista de estudiantes.
	listadoEstudiantes()
  #Esta línea toma una entrada del usuario en forma de número entero y la asigna a una variable "num_est".
	num_est = int(
	 input(
	  "\033[36m\n\n> Para volver al menú digite [0]\nIngrese el número de estudiante a actualizar los datos: "
	 ))
  #Si el número de estudiante ingresado es 0, se llama a una función llamada "main.regresarmenu()"
	if num_est == 0:
		main.regresarmenu()
  #Esta línea toma una entrada del usuario en forma de cadena y la asigna a la variable "nuevo_nombre".
	nuevo_nombre = input("Ingrese nombre y apellido del estudiante: ")
  #Esta línea toma una entrada del usuario en forma de cadena y la asigna a la variable "nueva_carrera".
	nueva_carrera = input("Ingrese la carrera del estudiante: ")
  #Esta línea actualiza el nombre del estudiante en el diccionario "db" con el nuevo nombre especificado.
	db["Estudiantes"][num_est - 1] = nuevo_nombre
  #Esta línea actualiza la carrera del estudiante en el diccionario "db" con la nueva carrera especificada.
	db["Carrera_estudiantes"][num_est - 1] = nueva_carrera
  #Esta línea limpia la pantalla del terminal.
	system("clear")
  #Esta línea imprime un mensaje indicando que la información del usuario ha sido actualizada.
	print("\033[0mInformación actualizada del usuario")
  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Estudiantes" en el diccionario "db".
	for i in range(len(db["Estudiantes"])):
    #Esta línea verifica si el nombre y la carrera del estudiante actual en el índice del bucle son iguales al nuevo nombre y la nueva carrera especificados. Si se cumple, se imprime el número del estudiante, el nuevo nombre y la nueva carrera en verde.
		if db["Estudiantes"][i] == nuevo_nombre and db["Carrera_estudiantes"][
		  i] == nueva_carrera:
			print("\033[32m{:^8}{:^20}{:^25}".format(i + 1, nuevo_nombre,
			                                         nueva_carrera))
    #caso contrario 
		else:
      # s implime el número del estudiante, el nuevo nombre y la nueva carrera en blanco.
			print("\033[0m{:^8}{:^20}{:^25}".format(i + 1, db["Estudiantes"][i],
			                                        db["Carrera_estudiantes"][i]))



def registroDevolucionLibros(numero_estudiante):
	"""
  Funcion: La función "registroDevolucionLibros()" verifica si un estudiante tiene un préstamo activo, en caso de tenerlo

 Parametros: numero_estudiante

 Retorna: retorna un valor booleano (verdadero o falso).
 	"""
  #Esta línea verifica si el estudiante actual tiene un préstamo activo, verificando en el campo "Prestamo_activo" del diccionario "db" con el número del estudiante-1.
	if db["Prestamo_activo"][numero_estudiante-1] == "Si":
    #Si se cumple la condición del if, se reduce en 1 el número de libros reservados del estudiante en el diccionario "db".
		db["Numero_libros_reservados"][numero_estudiante-1] -= 1
    #Se agrega el nombre del estudiante en el campo "Registro_devolucion" del diccionario "db"
		db["Registro_devolucion"].append((db["Estudiantes"][numero_estudiante-1]))
    #Se retorna verdadero
		return True
  #Si no se cumple la condición del if, se retorna falso.
	return False

def mostrarInforme():
	"""
  Funcion: La función "mostrarInforme()" genera un informe sobre los libros y los estudiantes en el diccionario "db", mostrando el nombre de los libros, el número de copias disponibles, el nombre de los estudiantes, el número de libros reservados, el número de libros prestados, el número de multas y el número

 Parametros: No, contiene ningun parametro 

 Retorna: No, retorna ningun dato 
 	"""
  #Esta línea limpia la pantalla del terminal.
	system("clear")
  #Esta línea imprime un mensaje indicando que se está generando un informe.
	print("Generando Informe...\n")
  #Estas líneas inicializan contadores para las variables total_copias, total_libros_reservados, total_libros_prestados, total_multas y total_visitas en 0.
	total_copias = total_libros_reservados=total_libros_prestados= total_multas = total_visitas= 0
  #Esta línea imprime un encabezado para los libros.
	print("\t\t\t\tLibros\n___________________________________________________________")
	print("\033[36m{:^40}{:^20}".format("Libro", "Número de copias"))
  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Titulos_libros" en el diccionario "db".
	for i in range(len(db["Titulos_libros"])):
    #Estas líneas imprimen el título de cada libro y el número de copias disponibles en el diccionario "db".
		print("\033[0m{:^40}{:^20}".format(db["Titulos_libros"][i],db["Copias_disponibles"][i]))
    #Esta línea suma el número de copias disponibles de cada libro a la variable total_copias.
		total_copias += int(db["Copias_disponibles"][i])
  #Esta línea imprime una línea de separación y el total de copias de los libros en el diccionario "db".
	print("___________________________________________________________")
	print("\033[33m{:^40}{:^20}".format("Total",total_copias))
  #Esta línea imprime un encabezado para los estudiantes.
	print("\t\n\n\033[0mEstudiantes\n_______________________________________________________________________________________________")
	print("\033[36m{:^20}{:^20}{:^20}{:^10}{:^26}".format("Estudiante","Libros reservados","Libros_prestados","Multas","Visitas a la Biblioteca"))
  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Estudiantes" en el diccionario "db".
	for i in range(len(db["Estudiantes"])):
    #Estas líneas imprimen el nombre del estudiante, el número de libros reservados, el número de libros prestados, el número de multas y el número de visitas de cada estudiante en el diccionario "db"
		print("\033[0m{:^20}{:^20}{:^20}{:^10}{:^26}".format(db["Estudiantes"][i], db["Numero_libros_reservados"][i],db["Numero_libros_prestados"][i],db["Numero_multas"][i],db["Numero_Visitas_Estudiante"][i]))
    #Estas líneas suman el número de libros reservados, el número de libros prestados, el número de multas y el número de visitas de cada estudiante en el diccionario "db" a las variables correspondientes.
		total_libros_reservados += db["Numero_libros_reservados"][i]
		total_libros_prestados += db["Numero_libros_prestados"][i]
		total_multas += db["Numero_multas"][i]
		total_visitas += db["Numero_Visitas_Estudiante"][i]
    #Esta línea imprime una línea de separación y el total de estudiantes, libros reservados, libros prestados, multas y visitas en el diccionario "db".
	print("_______________________________________________________________________________________________")
	print("\033[33m{:^20}{:^20}{:^20}{:^10}{:^26}".format("Total", total_libros_reservados,total_libros_prestados,total_multas,total_visitas))
			

def obtenerVisitasBiblioteca():
	"""
  Funcion: La funcion "obtenerVisitasBiblioteca()" es utilizada para obtener información estadística sobre las visitas a la biblioteca de los estudiantes registrados en el diccionario "db". En particular, se calcula el promedio de visitas, el número máximo de visitas y el número mínimo de visitas. Además, se imprime un listado con el número, el nombre del estudiante y el número de visitas a la biblioteca de cada estudiante.

 Parametros:No, contiene parametros

 Retorna: No, retorna ningun dato 
 	"""
  #Estas líneas inicializan contadores para las variables promedio_visitas, suma_visitas, n y los valores máximo y mínimo en 0.
	promedio_visitas = suma_visitas = n = 0
	maximo = max(db["Numero_Visitas_Estudiante"])
	minimo = min(db["Numero_Visitas_Estudiante"])
  #Esta línea imprime un encabezado con el número, el estudiante y el número de visitas a la biblioteca.
	print("\033[0m{:^8}\033[33m{:^20}\033[32m{:^21}".format(
	 "Número", "Estudiante", "Número de visitas"))
  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Estudiantes" en el diccionario "db".
	for i in range(len(db["Estudiantes"])):
    #Estas líneas imprimen el número, el nombre del estudiante y el número de visitas a la biblioteca de cada estudiante en el diccionario "db".
		print("\033[0m{:^8}{:^20}{:^21}".format(i + 1, db["Estudiantes"][i],
		                                        db["Numero_Visitas_Estudiante"][i]))
    #Esta línea suma el número de visitas a la biblioteca de cada estudiante en el diccionario "db" a la variable suma_visitas.
		suma_visitas = suma_visitas + db["Numero_Visitas_Estudiante"][i]
    #Esta línea aumenta el contador de n en 1.
		n = n + 1
  #Esta línea calcula el promedio de visitas a la biblioteca dividiendo la suma de visitas entre el número de estudiantes.
	promedio_visitas = suma_visitas / n
  #Estas líneas imprimen el promedio de visitas a la biblioteca   
	print(
	 f"\nEl promedio de visitas a la biblioteca: {round(promedio_visitas,2)}")
  # imprime la cantidad de visitas máximas
	print(f"La cantidad de visitas máximas a la biblioteca es: {maximo}")
  # imprime la cantidad de visitas mínimas a la biblioteca.
	print(f"La cantidad de visitas mínimas a la biblioteca es: {minimo}")



def obtenerLibrosPrestados():
	"""
  Funcion: Esta función se encarga de calcular el total de libros prestados y el total de multas generadas.
Además, se genera una gráfica de barras mostrando el número de multas por estudiante.

 Parametros: No, contiene ningun parametro 

 Retorna: No, retorna ningun dato o valor 
 	"""
  # Inicializamos variables para almacenar la suma de los libros prestados y las multas generadas
	numero_libros_prestados = numero_multas = 0
  #Inicializamos dos listas vacias para almacenar los estudiantes y las multas generadas
	lista_estudiantes = y = []
  #Se recorre el numero de estudiantes existentes en el diccionario "db"
	for i in range(len(db["Estudiantes"])):
    #Sumamos los libros prestados de cada estudiante
		numero_libros_prestados = numero_libros_prestados + db[
		 "Numero_libros_prestados"][i]
    #Sumamos las multas generadas de cada estudiante
		numero_multas += db["Numero_multas"][i]
    #Agregamos el nombre del estudiante a la lista
		lista_estudiantes.append(db["Estudiantes"][i])
    ##Agregamos el numero de multas generadas por el estudiante a la lista
		y.append(db["Numero_multas"][i])
	print("El Total de libros prestados es: ", numero_libros_prestados)
	print("El Total de multas generadas es: ", numero_multas)
  ##generamos un grafica de barras con las multas generadas por cada estudiante
	graficas.bar(lista_estudiantes, y, color='red')
  #mostramos el nombre de los estudiantes en el eje x
	graficas.xticks(lista_estudiantes)
	graficas.title("Gráfica estudiantes y numero de multas")
  #mostramos la grafica
	graficas.show()


def seguimientoHorasTrabajadasPersonal():
	"""
 	 Funcion: Esta función que muestra las horas trabajadas por cada personal 

   Parametros: No, contiene parametros

  Retorna: No, retorna ningun valor 
  	"""
	print("\n\033[0m{:^8}\033[33m{:^30}\033[32m{:^19}".format("Número", "Nombre","Horas Trabajadas"))
	for i in range(len(db["Personal"])):
		 #Esta línea imprime un encabezado con el número, el estudiante y el número de visitas a la biblioteca.
		print("\033[0m{:^8}{:^30}{:^19}".format(i+1, db["Personal"][i],db["Horas_trabajas"][i]))

def informacionDelPersonal():
	"""
 	 Funcion: Esta función que obtiene la informacion de cada personal que trabaja en la biblioteca

   Parametros: No, contiene parametros

  Retorna: No, retorna ningun valor 
  	"""
	  #Esta línea inicia un bucle "for" que iterará a través del rango de la longitud del campo "Personal" en el diccionario de la base de datos "db".
	print("\n\033[0m{:^8}\033[33m{:^30}\033[32m{:^25}\033[33m{:^9}\033[33m{:^17}".format("Número", "Nombre", "Cargo", "Salario","Jornada Laboral"))
	for i in range(len(db["Personal"])):
		 #Esta línea imprime un encabezado con el número, el estudiante y el número de visitas a la biblioteca.
		print("\033[0m{:^8}{:^30}{:^25}{:^9}{:^17}".format(i+1, db["Personal"][i], db["Cargo"][i], "$"+db["Salarios"][i], db["Jornada_laboral"][i]))
		
	
	

def obtenerHistorialReservasPrestamos(nombre_estudiante):
	"""
 	 Funcion: La función "obtenerHistorialReservasPrestamos" tiene como parámetro "nombre_estudiante", el cual es el nombre del estudiante del cual se quiere obtener el historial de reservas y préstamos.

 Parametros: nombre_estudiante 

 Retorna: No, retorna ningun dato o valor
  	"""
  #Se utiliza un método split() para dividir el nombre en una lista con los nombres y apellidos.
	nombre = nombre_estudiante.split()
  #Se utiliza un ciclo for para recorrer la lista de estudiantes en la base de datos.
	for i in range(len(db["Estudiantes"])):
    #Se utiliza una condición if para verificar si el nombre del estudiante en la base de datos es igual al nombre ingresado como parámetro.
		if db["Estudiantes"][i].lower() == nombre_estudiante:
      #Si se cumple la condición, se imprime una cadena de texto con información sobre los libros prestados, libros reservados, el total de préstamos y el total de reservas del estudiante.
			print(
			 f"""\nHistorial de {db["Estudiantes"][i]}\n\033[36mLibros Prestados: \033[0m{db["Libros_reservados_"+nombre[0]+"_"+nombre[1]]}\n\033[36mLibros Reservados: \033[0m{db["Libros_prestados_"+nombre[0]+"_"+nombre[1]]}\n\033[36mTotal Prestamos: \033[0m{db["Numero_libros_reservados"][i]}\n\033[36mTotal Reservas: \033[0m{db["Numero_libros_prestados"][i]}"""
			)


def mostrarSalas():
	"""
  Funcion: La función mostrarSalas() imprime en pantalla una tabla con la información de las salas de estudio.

 Parametros: No contiene parametros 

 Retorna: No terorna ningun valor 
 	"""
  #La primera línea utiliza el método "print" para imprimir una cadena de texto con formato especifico
	print("\033[0m{:^8}\033[33m{:^18}\033[32m{:^17}".format(
	 "Número", "Sala de Estudio", "Disponibilidad"))
  #La segunda línea es un ciclo "for" que recorre la lista "db["Salas_de_estudio"]" y utiliza el método "print" para imprimir una línea por cada elemento de la lista, con el formato especificado en la primera línea
	for i in range(len(db["Salas_de_estudio"])):
    #La función imprime el numero de la sala, el nombre de la sala y su disponibilidad.
		print("\033[0m{:^8}{:^18}{:^17}".format(i+1, db["Salas_de_estudio"][i], db["Sala_disponible"][i]))
			
def disponibilidadSala(numero_sala,numero_estudiante):
	"""
    Funcion: La función es asignar una sala de estudio específica como "no disponible" y registrar que la sala ha sido reservada por un 
     estudiante específico.
    La función recibe dos parametros, el numero de la sala y el numero del estudiante, y verifica si la sala esta disponible, si lo esta cambia 
    el estado de disponibilidad a no y registra el estudiante que reservo la sala.

 Parametros: numero_sala,numero_estudiante

 Retorna: false or true 
 	"""
	#La segunda línea es una condicional en la cual se comprueba si la sala seleccionada está disponible.
	if db["Sala_disponible"][numero_sala-1] == "Si":
	  #si la condición se cumple, cambia el estado de la sala a "No disponible"
		db["Sala_disponible"][numero_sala-1] = "No"
	  #se guarda el nombre de la sala reservada en el registro del estudiante correspondiente.
		db["Sala_reservada"][numero_estudiante-1] = db["Salas_de_estudio"][numero_sala-1]
	    #retorna verdadero
		return True
	    #retorna falso 
	return False

#Complejidad tiempo y espacio
def complejidad_Big_o(datos,numproceso):
	# creamos un generador de datos
	generador_datos = lambda n: datos
	match numproceso:
		case 1:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(registro_estudiante, generador_datos)
		case 2:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(buscarLibro, generador_datos)
		case 3:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(actualizarLibrosReservados, generador_datos)
		case 4:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(registro_estudiante, generador_datos)
		case 5:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(registro_estudiante, generador_datos)
		case 6:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(registro_estudiante, generador_datos)
		case 7:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(registro_estudiante, generador_datos)
		case 8:
			#calculamos la complejidad del algoritmo
			best, others = big_o.big_o(registro_estudiante, generador_datos)
	#imprimimos la complejidad del algoritmo
	print(f"Complejidad del proceso [{numproceso}]: {best}")
	