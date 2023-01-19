from image_to_ascii import ImageToAscii
from replit import Database
from os import system
import os,estudiante,Biblioteca,baseDatos,time

db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzQyMDIzODQsImlhdCI6MTY3NDA5MDc4NCwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.0AECGjcAlygu1w-9wOyuqOXav5BjfLZg67FdeQua-k84gywG6RwxGAsSmSk7d0o4AvHquo_H2hdo3SexlW6z0Q")

def cargarImagen():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	ImageToAscii(imagePath="libro.png",witdh=100,outputFile="output.txt")
	fichero = open('output.txt')
	print(fichero.read())
	time.sleep(5)
	system("clear")

def cargarLogo():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	print("*************BiblioSolution*************")
	fichero = open('output.txt')
	print(fichero.read())
	time.sleep(5)
	system("clear")
	
def regresarmenu():
	"""
  Funcion:

 Parametros:

 Retorna:
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
9.- Servicios en línea: permite a los usuarios buscar y reservar materiales en línea
10.- Registro de devolución de los libros
11.- Generar informe de la biblioteca
12.- Estadísticas sobre el número de visitas a la biblioteca
13.- Estadísticas del número de libros prestados, el número de multas
14.- Sistema de gestión de la biblioteca
15.- Historial de préstamos
16.- Reservas de salas de estudio
17.- Calculo Complejidad de tiempo y espacio 
18.- Salir
----------------------------------
"""

def menu():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	print(f"\033[36m{mensajePrincipal}")
	while True:
	    try:
	        opcion = int(input("\033[0mIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	        system("clear")
	        menu()
	match opcion:
		case 1:
			system('clear')
			print("\033[0m---Registro estudiante---\n")
			estudiante.registro()
		case 2:
			system('clear')
			print("\033[0m---Catálogo BiblioSolutions---\n")
			Biblioteca.catalogo()
		case 3:
			system('clear')
			print("\033[0m---Reserva de libros---\n")
			Biblioteca.ingresoDatosParaReservaOPrestamoLibro(1)
		case 4:
			system('clear')
			print("\033[0m---Prestamo de libros---\n")
			Biblioteca.ingresoDatosParaReservaOPrestamoLibro(2)
		case 5:
			system('clear')
			print("\033[0m---Notificaciones---\n")
			print(">Se han enviado notificaciones a los siguientes usuarios")
			estudiante.notificacion()
		case 6:
			system('clear')
			print("\033[0m---Seguimiento libros---\n")
			baseDatos.seguimientoLibros()
		case 7:
			system('clear')
			print("\033[0m---Gestión de usuarios---\n")
			baseDatos.actualizarUsuario()
		case 8:
			system('clear')
			print("\033[0m---Sistema de multas---\n")
			
		case 9:
			system('clear')
			print("\033[0m---Servicios en línea---\n")
			
		case 10:
			system('clear')
			print("\033[0m---Registro de devolución de los libros---\n")
			Biblioteca.registroDevolucionLibros()
		case 11:
			system('clear')
			print("\033[0m---Generar informe de la biblioteca---\n")
			Biblioteca.generarInforme()
		case 12:
			system('clear')
			print("\033[0m---Estadísticas sobre el número de visitas a la biblioteca---\n\n")
			baseDatos.obtenerVisitasBiblioteca()
		case 13:
			system('clear')
			print("\033[0m---Estadísticas del número de libros prestados, el número de multas---\n")
			baseDatos.obtenerLibrosPrestados()
		case 14:
			system('clear')
			print("\033[0m---Sistema de gestión de la biblioteca---\n")
			
		case 15:
			system('clear')
			print("\033[0m---Historial de préstamos---\n")
			estudiante.historialPrestamosReservas()
		case 16:
			system('clear')
			print("\033[0m---Reservas de salas de estudio---\n")
			Biblioteca.reservaSala()
		case 17:
			print("\033[0m---Calculo Complejidad tiempo y espacio---\n")
		case 18: 
			print("\033[36mGracias... ¡Vuelve pronto!")
			exit()
		case 19:
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
	#baseDatos.cargarDBEstudiantes()
	#se carga las salas
	#baseDatos.cargarSalas()
	#cargarImagen()
	cargarLogo()
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