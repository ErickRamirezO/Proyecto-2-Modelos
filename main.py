from image_to_ascii import ImageToAscii
from replit import Database
from os import system
import estudiante,Biblioteca,baseDatos,time,complejidad,os

db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzQ2MDA2NTEsImlhdCI6MTY3NDQ4OTA1MSwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.B3_FtPfYaWeH5xbOMyd2PeDLqQdEtEZoP2LTlaMxos9UU8OqEAThrHT3_xa0MXoOyJv15a3aMlr0MHUbAZmsgg")

def cargarImagen():
	"""
  Funcion: La funcion carga una imagen 

 Parametros: No, contiene parametros 
 
 Retorna: No, retorna ningun dato
 	"""
  #sta linea utiliza la funcion "ImageToAscii" para convertir una imagen especificada en el parametro "imagePath" con ancho especificado en "width" y guarda el resultado en un archivo de texto especificado en "outputFile"
	ImageToAscii(imagePath="libro.png",witdh=100,outputFile="output.txt")
  #abre el archivo de texto creado en el paso anterior
	fichero = open('output.txt')
  # imprime el contenido del archivo de texto
	print(fichero.read())
  # detiene la ejecución del codigo por 5 segundos
	time.sleep(5)
  #limpia la pantalla del terminal
	system("clear")

def cargarLogo():
	"""
  Funcion: La funcion nos va a mostrar un catalogo del software 

 Parametros: No, contiene ningun parametro 

 Retorna: No, retorna ningun dato
 	"""
  #La primera línea imprime un título "BiblioSolution" en consola.
	print("*************BiblioSolution*************")
  #La segunda línea abre un archivo llamado 'output.txt' y lo asigna a la variable fichero.
	fichero = open('output.txt')
  #La tercera línea imprime el contenido del archivo 'output.txt' en consola.
	print(fichero.read())
  #detiene la ejecución del programa por 5 segundos.
	time.sleep(5)
  # línea limpia la consola.
	system("clear")
  #llama a una función llamada "textoInicio()"
	textoInicio()
  #espera una entrada del usuario para continuar.
	input("\nPresione una tecla para poder iniciar ya con el programa :D")
  #limpia la consola de nuevo.
	system("clear")

def textoInicio():
	"""
  Funcion: La función textoInicio() imprime en consola un texto de introducción sobre el programa
 
 Parametros: No, contine ningun parametro

 Retorna: No, retorna ningun tipo de dato
 	"""
  #imprime una introduccion del programa 
	texto = """BiblioSolutions\n
 Es un programa que permite la gestión de una biblioteca desarrollado\n100% en Python. Este tipo de software ofrece una variedad de funciones como:\n> la adición y eliminación de registros de libros\n> Gestión de préstamos y devoluciones\n> Generación de informes\n> Estadísticas\n> Busqueda de libros en la base de datos de la biblioteca.\n\n"""
	#imprime una guia de inicio del programa
	guia = """1) Use el menú de  opciones\nEscoja la opción que desee entre los 16 que se dispone (recuerde ingresar el dato correcto y lea detenidamente)\n2) Registrar usuario\nAquí puede registrar a un usuario siguiendo todos los pasos e ingresando los datos que pida el sistema.\n3)Revisión de catalogo\nPermite buscar y encontrar los diferentes libros ya sea por Titulo o Autor.\n4)Notificaciones\nPuede enviar un aviso a los usuarios para que devuelvan los libros que han solicitado\n5) Estadísticas\nPuede consultar el numero de visitas, numero de multas, numero de libros prestados etc.\n6) Salas de estudio\nPermite al estudiante reservar una sala si es que se encuentra disponible\n"""
  #Utiliza un bucle para imprimir cada letra del texto de forma individual
	for letra in texto:
	    print(letra, end="", flush=True)
    #retraso de 0.01 segundos entre cada impresión
	    time.sleep(0.01)
	##espera una entrada del usuario para continuar.
	input("\nPresione una tecla para ver la guia de inicio rapido")
	#limpiamos la pantalla
	system("clear")
	#imprime mensaje de que a continuacion es la guia de inicio rapido
	print("\033[36m\t\tGuía de inicio Rápido\033[0m")
	 #Utiliza un bucle para imprimir cada letra del texto de forma individual
	for letra in guia:
	    print(letra, end="", flush=True)
    #retraso de 0.01 segundos entre cada impresión
	    time.sleep(0.01)
def regresarmenu():
	"""
  Funcion: Esta función permite regresar al menu principal si es que se encuentra dentro de una opcion

 Parametros: No tiene parámetros

 Retorna: No retorna ningún valor
 	"""
	system("clear")
	menu()
	
#variable mensaje que contiene todo el menú de opciones escrito
mensajePrincipal = """BiblioSolutions 📚
----------------------------------
1 - Registrar un estudiante por carrera
2 - Catálogo: buscar y encontrar libros, revistas, tesis, etc.
3 - Reserva de libros
4 - Prestamo de libros
5.- Notificaciones
6.- Seguimiento libros
7.- Gestión de usuarios
8.- Sistema de multas
9.- Servicios en línea: buscar libros, novedades, validar ISBN
10.- Registro de devolución de los libros
11.- Generar informe de la biblioteca
12.- Estadísticas sobre el número de visitas a la biblioteca
13.- Estadísticas del número de libros prestados, el número de multas
14.- Sistema de gestión de personal de la biblioteca
15.- Historial de préstamos
16.- Reservas de salas de estudio
17.- Calculo Complejidad de tiempo y espacio 
18.- Salir
----------------------------------
"""

def menu():
	"""
  Funcion: L afuncion menu, nos mostrara en pantalla todos los procesos que tiene el software 

 Parametros: No, contiene ningun parametro

 Retorna: No, retorna ningun dato 
 	"""
	print(f"\033[36m{mensajePrincipal}")
  #el bucle while para que el usuario ingrese la opcion correcta
	while True:
	    try:
        #mensaje de ingreso de opcion
	        opcion = int(input("\033[0mIngrese una opción: "))
	        break
        # si la opcion ingresada por el usuario es incorrecta nos mostara un error 
	    except ValueError:
        #mensaje que pide al usuario que ingrese de nuevo la opcion correcta
	        print("\033[31mEntrada inválida, ingrese solo numeros")
        #limpia la pantalla
	        system("clear")
        # muestra el menu de opciones 
	        menu()
        
	match opcion:
  #primer caso 
		case 1:
      #limpia la pantalla 
			system('clear')
      # mensaje del registro de estudiante 
			print("\033[0m---Registro estudiante---\n")
      # se guarda en la funcion de registro de estudiante 
			estudiante.registro()
    #segundo caso 
		case 2:
      #limpia la pantalla 
			system('clear')
      # mensaje del catalago de la biblioteca 
			print("\033[0m---Catálogo BiblioSolutions---\n")
      # se guarda en la funcion de catalogo 
			Biblioteca.catalogo()
    # tercer caso 
		case 3:
      #limpia l pantalla 
			system('clear')
      #mensaje de reserva de libros 
			print("\033[0m---Reserva de libros---\n")
      #se guarda en la funcion de ingresoDatosParaReservarOPrestamoLibro
			Biblioteca.ingresoDatosParaReservaOPrestamoLibro(1)
    #cuarto caso 
		case 4:
      #limopiar pantalla 
			system('clear')
      #muestra la opcion de prestamo del libro
			print("\033[0m---Prestamo de libros---\n")
      #llama  a la funcion 
			Biblioteca.ingresoDatosParaReservaOPrestamoLibro(2)
    #quinto caso
		case 5:
      #limpia la pantalla
			system('clear')
      #mensaje de notificacion
			print("\033[0m---Notificaciones---\n")
      #llamamos a la funcion de notificacion
			estudiante.notificacion()
    #sexto caso 
		case 6:
      #limpia la pantalla 
			system('clear')
      #muestra la opcion del siguimiento de libros
			print("\033[0m---Seguimiento libros---\n")
      #llamamos a la funcion de seguimiento de libros 
			baseDatos.seguimientoLibros()
    #septimo caso
		case 7:
      #limpia la panatalla
			system('clear')
      #opcion de gestion de usuarios 
			print("\033[0m---Gestión de usuarios---\n")
      #llamamos a la funcion de actualizar usuario 
			Biblioteca.actualizarEstudiante()
    #octavo caso
		case 8:
      #limpiamos la pantalla
			system('clear')
      #opcion de las multas 
			print("\033[0m---Sistema de multas---\n")
      #llamamos a la funcion de sistema de multas 
			baseDatos.sistemaMulta(1)
    #noveno caso 
		case 9:
      #limpia la pantalla
			system('clear')
      #opcion del servicio en linea de la Biblioteca
			print("\033[0m---Servicios en línea---\n")
      #llamamos a la funcion de servicios en linea 
			baseDatos.masServiciosCatalogo(1)
    #decimo caso 
		case 10:
      #limpia la pantalla 
			system('clear')
      #opcion de registro de devolucion de los libros 
			print("\033[0m---Registro de devolución de los libros---\n")
      #llamamos a la funion de registro de devolucion de libros 
			Biblioteca.registroDevolucionLibros()
    # onceavo caso
		case 11:
      #limpia la pantalla 
			system('clear')
      #opcion de generar informes de la Biblioteca
			print("\033[0m---Generar informe de la biblioteca---\n")
      #llamamos a la funcion generar informes 
			Biblioteca.generarInforme(1)
    #doceavo caso 
		case 12:
      #limpia la pantalla 
			system('clear')
      #opcion de mostrar la estadistica sobre las visitas en la Biblioteca
			print("\033[0m---Estadísticas sobre el número de visitas a la biblioteca---\n\n")
      #llamamos a la funcion de obtener la vista en la Biblioteca
			baseDatos.obtenerVisitasBiblioteca(1)
    #treceavo caso
		case 13:
      #limpia la pantalla
			system('clear')
      #opcion de estadistica del numero de los libros prestados 
			print("\033[0m---Estadísticas del número de libros prestados, el número de multas---\n")
      #llamamos a la funcion de obtener libros prestados, esto para hacer la estadistica 
			baseDatos.obtenerLibrosPrestados(1)
    #catorceavo caso
		case 14:
      #limpia la pantalla 
			system('clear')
      #opcion de sistema de gestion de la Biblioteca
			print("\033[0m---Sistema de gestión de personal de la biblioteca---\n")
	#llamamos a la función de gestionDePersonal
			Biblioteca.gestionDePersonal()
	# quinceavo caso
		case 15:
      #limpia la pantalla 
			system('clear')
      # opcion de historia de prestamos 
			print("\033[0m---Historial de préstamos---\n")
      #llamamos a la funcion del historial de prestamo que tenga la Biblioteca
			estudiante.historialPrestamosReservas()
    #sexteavo caso 
		case 16:
      #limpia la pantalla 
			system('clear')
      #opcion de reservas de la sala de estudiante para estudiar 
			print("\033[0m---Reservas de salas de estudio---\n")
      #llamamos a la funcion de reserva de la sala 
			Biblioteca.reservaSala()
    #caso numero 17
		case 17:
      #opcion para que se pueda calcular la complejidad ya sea de tiempo o espacio
			print("\033[0m---Calculo Complejidad tiempo y espacio---\n")
      #llamamos a la funcion 
			complejidad.menuComplejidad()
    # caso numero 18 
		case 18: 
      #mensaje de agradecimiento por usar esl software de la Biblioteca
			print("\033[36mGracias... ¡Vuelve pronto!")
      #cierra el programa 
			exit()
    #caso numero 19  
		case 19:
      #mensaje de imprime datos 
			print("Datos\n")
			keys = db. keys( )
			#print(db["Estudiantes"])
			for key in keys:
				print(f"""\n{key}: {db[key]}""")
			#print(db["Estudiantes"])
		case _:
			print("\033[31mIngrese una opción válida")


if __name__ == "__main__":
	#Se carga la base de datos de libros
	#baseDatos.cargarDBLibros()
	#Se carga la base de datos de estudiantes
	baseDatos.cargarDBEstudiantes()
	#se carga las salas
	#baseDatos.cargarSalas()
	#se carga el personal
	#baseDatos.cargarPersonal()
	#cargarImagen()
	#cargarLogo()
	while True:
		#Limpiamos la pantalla
		system('clear')
		#print(os.getenv("REPLIT_DB_URL"))
		#llamada a la función menu
		menu()
		#solicitamos al usuario que persione cualquier tecla
		#para continuar con el programa
		input("\n\033[0mPresione una tecla para continuar... ")

		#del db["Carrera"]
		#keys = db.keys()
		#for key in keys:
		#	print(f"""{key}: {db[key]}""")
		#print(os.getenv("REPLIT_DB_URL"))