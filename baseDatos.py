from replit import Database
from memory_profiler import profile
import big_o, os, main
import datos as Datos
from os import system
import matplotlib.pyplot as graficas

db = Database(
 "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzQyMDIzODQsImlhdCI6MTY3NDA5MDc4NCwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.0AECGjcAlygu1w-9wOyuqOXav5BjfLZg67FdeQua-k84gywG6RwxGAsSmSk7d0o4AvHquo_H2hdo3SexlW6z0Q"
)


def cargarDBLibros():
	"""
 Funcion: carga una base de datos de libros. Primero, imprime un mensaje indicando que se está cargando la base de datos. Luego, asigna un 
          arreglo vacío a cada una de las categorías de la base de datos.

 Parametros: Ninguno 

 Retorna: no retorna nada 
 
 	"""
  #mensaje de que se esta cargando la base de datos de los libros 
	print("Cargando base de datos libros...")
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
	print("Cargando base de datos de estudiantes...")
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
	print("Cargando salas...")
	#lista con las categorias salas de estudio, sala disponible y sala reservada
	db["Salas_de_estudio"] = db["Sala_disponible"]= db["Sala_reservada"]=[]
  #  En un ciclo "for", agrega los datos correspondientes a cada una de las categorías a partir de los datos contenidos en una clase llamada 
  #  "Datos"
	for i in range(len(Datos.salas)):
    #los datos correspondientes a cada una de las categorías
		db["Salas_de_estudio"].append(Datos.salas[i])
    #los datos correspondientes a cada una de las categorías
		db["Sala_disponible"].append(Datos.sala_disponible[i])
    #los datos correspondientes a cada una de las categorías
		db["Sala_reservada"].append(Datos.sala_reservada[i])
		
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


def registro_estudiante(nombre, carrera):
	"""
 Funcion: La funcion se encarga de registrar un nuevo estudiante en la base de datos.

 Parametros: nombre, carrera

 Retorna: Retorna un mensaje 
 	"""
  #Primero, utiliza un ciclo "for" para recorrer la lista de estudiantes existentes en la base de datos. 
	for i in range(len(db["Estudiantes"])):
    #Utiliza el método "in" para verificar si el nombre del estudiante ingresado ya existe en la lista.
		if str(nombre) in db["Estudiantes"][i]:
      #mensaje de ingreso del nombre ya existio 
			print("\033[31mEl nombre ingresado ya existe")
  #Si el nombre no existe, agrega el nombre del estudiante, la carrera, el número de libros reservados y el número de visitas a la base de datos. 
	else:
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


def actualizarLibrosReservados(nombre_estudiante, numeroLibroReservar,
                               reserva_o_prestamo):
	"""
  Funcion: La funcion actualiza la base de datos de acuerdo a la acción de reservar o prestar un libro.

 Parametros: nombre_estudiante, numeroLibroReservar,reserva_o_prestamo

 Retorna: No, retorna ningun dato o valor 
 	"""
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
				print("\033[32m ¡Ejemplar reservado con éxito!")
      #En caso de ser 2, se aumenta en 1 el número de libros prestados del estudiante y se agrega el título del libro prestado a la lista de libros
			else:
				db["Numero_libros_prestados"][i] = db["Numero_libros_prestados"][i] + 1
				db["Libros_prestados_" + nombre[0] + "_" + nombre[1]].append(
				 db["Titulos_libros"][numeroLibroReservar])
        #mesaje de que se va a prestar el libro 
				print("\033[32m ¡Ejemplar prestado con éxito!")



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
  
	if db["Numero_libros_reservados"][numero_estudiante - 1] > 0:
		total_libros = db["Numero_libros_reservados"][numero_estudiante - 1]
		nombre_estudiante = db["Estudiantes"][numero_estudiante - 1]
		db["Notificacion_devolucion"][
		 numero_estudiante - 1] = "¡Aviso! Tiene " + str(
		  total_libros) + " libros pendientes por devolver"
		print(
		 f"\033[32m Se ha notificado satisfactoriamente al estudiante \033[0m{nombre_estudiante}"
		)
	else:
		print("No se puede enviar la notificación al estudiante " +
		      db["Estudiantes"][numero_estudiante - 1] +
		      " porque no tiene reservado ningún libro")
		input("Presione cualquier tecla para escoger otro estudiante")
		system("clear")
		print("---Notificaciones---")
		print(
		 "Los estudiantes que tienen reservados libros se marcan de color \033[32mverde"
		)
		listadoEstudiantesReserva()
		while True:
			try:
				numero = int(
				 input("\nIngrese el número del estudiante para notificarle: "))
				break
			except ValueError:
				print("Por favor, ingrese solo números.")
				system("clear")
		notificarUsuario(numero)


#punto 6
def seguimientoLibros():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	print("\033[33m{:^40}{:^28}{:^14}{:^18}{:^40}{:^14}".format(
	 "Libros", "Autor", "Disponibilidad", "Número de copias", "Ubicacion",
	 "Conservación"))
	for i in range(len(db["Titulos_libros"])):
		print("\033[0m{:^40}{:^28}{:^14}{:^18}{:^40}{:^9}".format(
		 db["Titulos_libros"][i], db["Autores_libros"][i], db["Disponibilidad"][i],
		 db["Copias_disponibles"][i], db["Ubicacion"][i], db["Conservacion"][i]))


def validarbusquedaLibro(libro):
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	for i in range(len(db["Titulos_libros"])):
		if db["Titulos_libros"][i].lower() == libro or db["Autores_libros"][i].lower(
		) == libro:
			return True
	return False


def buscarLibro(libro):
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	for i in range(len(db["Titulos_libros"])):
		if db["Titulos_libros"][i].lower() == libro or db["Autores_libros"][i].lower(
		) == libro:
			print(
			 f"""\n\033[0m Se encontró el siguiente libro\n\n\033[33m{db["Titulos_libros"][i]} de {db["Autores_libros"][i]}"""
			)
			print(f"""\033[0mDisponible: \033[36m{db["Disponibilidad"][i]}""")


#punto 7
def actualizarUsuario():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	listadoEstudiantes()
	num_est = int(
	 input(
	  "\033[36m\n\n> Para volver al menú digite [0]\nIngrese el número de estudiante a actualizar los datos: "
	 ))
	if num_est == 0:
		main.regresarmenu()
	nuevo_nombre = input("Ingrese nombre y apellido del estudiante: ")
	nueva_carrera = input("Ingrese la carrera del estudiante: ")
	db["Estudiantes"][num_est - 1] = nuevo_nombre
	db["Carrera_estudiantes"][num_est - 1] = nueva_carrera
	system("clear")
	print("\033[0mInformación actualizada del usuario")
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i] == nuevo_nombre and db["Carrera_estudiantes"][
		  i] == nueva_carrera:
			print("\033[32m{:^8}{:^20}{:^25}".format(i + 1, nuevo_nombre,
			                                         nueva_carrera))
		else:
			print("\033[0m{:^8}{:^20}{:^25}".format(i + 1, db["Estudiantes"][i],
			                                        db["Carrera_estudiantes"][i]))


#punto 10
def registroDevolucionLibros(numero_estudiante):
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	if db["Prestamo_activo"][numero_estudiante-1] == "Si":
		db["Numero_libros_reservados"][numero_estudiante-1] -= 1
		db["Registro_devolucion"].append((db["Estudiantes"][numero_estudiante-1]))
		return True
	return False

#punto11
def mostrarInforme():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	system("clear")
	print("Generando Informe...\n")
	total_copias = total_libros_reservados=total_libros_prestados= total_multas = total_visitas= 0
	print("\t\t\t\tLibros\n___________________________________________________________")
	print("\033[36m{:^40}{:^20}".format("Libro", "Número de copias"))
	for i in range(len(db["Titulos_libros"])):
		print("\033[0m{:^40}{:^20}".format(db["Titulos_libros"][i],db["Copias_disponibles"][i]))
		total_copias += int(db["Copias_disponibles"][i])
	print("___________________________________________________________")
	print("\033[33m{:^40}{:^20}".format("Total",total_copias))
	print("\t\n\n\033[0mEstudiantes\n_______________________________________________________________________________________________")
	print("\033[36m{:^20}{:^20}{:^20}{:^10}{:^26}".format("Estudiante","Libros reservados","Libros_prestados","Multas","Visitas a la Biblioteca"))
	for i in range(len(db["Estudiantes"])):
		print("\033[0m{:^20}{:^20}{:^20}{:^10}{:^26}".format(db["Estudiantes"][i], db["Numero_libros_reservados"][i],db["Numero_libros_prestados"][i],db["Numero_multas"][i],db["Numero_Visitas_Estudiante"][i]))
		total_libros_reservados += db["Numero_libros_reservados"][i]
		total_libros_prestados += db["Numero_libros_prestados"][i]
		total_multas += db["Numero_multas"][i]
		total_visitas += db["Numero_Visitas_Estudiante"][i]
	print("_______________________________________________________________________________________________")
	print("\033[33m{:^20}{:^20}{:^20}{:^10}{:^26}".format("Total", total_libros_reservados,total_libros_prestados,total_multas,total_visitas))
			
#punto 12
def obtenerVisitasBiblioteca():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	promedio_visitas = suma_visitas = n = 0
	maximo = max(db["Numero_Visitas_Estudiante"])
	minimo = min(db["Numero_Visitas_Estudiante"])
	print("\033[0m{:^8}\033[33m{:^20}\033[32m{:^21}".format(
	 "Número", "Estudiante", "Número de visitas"))
	for i in range(len(db["Estudiantes"])):
		print("\033[0m{:^8}{:^20}{:^21}".format(i + 1, db["Estudiantes"][i],
		                                        db["Numero_Visitas_Estudiante"][i]))
		suma_visitas = suma_visitas + db["Numero_Visitas_Estudiante"][i]
		n = n + 1
	promedio_visitas = suma_visitas / n
	print(
	 f"\nEl promedio de visitas a la biblioteca: {round(promedio_visitas,2)}")
	print(f"La cantidad de visitas máximas a la biblioteca es: {maximo}")
	print(f"La cantidad de visitas mínimas a la biblioteca es: {minimo}")


#punto 13
def obtenerLibrosPrestados():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	numero_libros_prestados = numero_multas = 0
	lista_estudiantes = y = []
	for i in range(len(db["Estudiantes"])):
		numero_libros_prestados = numero_libros_prestados + db[
		 "Numero_libros_prestados"][i]
		numero_multas += db["Numero_multas"][i]
		lista_estudiantes.append(db["Estudiantes"][i])
		y.append(db["Numero_multas"][i])
	print("El Total de libros prestados es: ", numero_libros_prestados)
	print("El Total de multas generadas es: ", numero_multas)
	graficas.bar(lista_estudiantes, y, color='red')
	graficas.xticks(lista_estudiantes)
	graficas.title("Gráfica estudiantes y numero de multas")
	graficas.show()

#punto 14
def gestionBiblioteca():
	pass
	
#punto 15
def obtenerHistorialReservasPrestamos(nombre_estudiante):
	"""
 	 Funcion:

 Parametros:

 Retorna:
  	"""
	nombre = nombre_estudiante.split()
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i].lower() == nombre_estudiante:
			print(
			 f"""\nHistorial de {db["Estudiantes"][i]}\n\033[36mLibros Prestados: \033[0m{db["Libros_reservados_"+nombre[0]+"_"+nombre[1]]}\n\033[36mLibros Reservados: \033[0m{db["Libros_prestados_"+nombre[0]+"_"+nombre[1]]}\n\033[36mTotal Prestamos: \033[0m{db["Numero_libros_reservados"][i]}\n\033[36mTotal Reservas: \033[0m{db["Numero_libros_prestados"][i]}"""
			)

#punto 16
def mostrarSalas():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	print("\033[0m{:^8}\033[33m{:^18}\033[32m{:^17}".format(
	 "Número", "Sala de Estudio", "Disponibilidad"))
	for i in range(len(db["Salas_de_estudio"])):
		print("\033[0m{:^8}{:^18}{:^17}".format(i+1, db["Salas_de_estudio"][i], db["Sala_disponible"][i]))
			
def disponibilidadSala(numero_sala,numero_estudiante):
	if db["Sala_disponible"][numero_sala-1] == "Si":
		db["Sala_disponible"][numero_sala-1] = "No"
		db["Sala_reservada"][numero_estudiante-1] = db["Salas_de_estudio"][numero_sala-1]
		return True
	return False