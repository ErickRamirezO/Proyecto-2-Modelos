from replit import Database
from os import system
import os,estudiante,Biblioteca,baseDatos

db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzM4MjAyNjYsImlhdCI6MTY3MzcwODY2NiwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.yvV7rTJBFyQ3focAr8tK0p1X7gLS85o6K04J_saXfpqUaXV7h4e0s5gq_Zc78PstwEhnUxCBDauGw5_tpp4cew")

#variable mensaje que contiene todo el menú de opciones escrito
mensajePrincipal = """Biblioteca 📚(nombre)
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
13.- Estadísticas del número de libros prestados, el número de multas, etc.
14.- Sistema de gestión de la biblioteca
15.- Historial de préstamos
16.- Reservas de salas de estudio
17.- Salir
----------------------------------
"""

def menu():
	print(f"\033[36m{mensajePrincipal}")
	opcion = int(input("\033[33mIngresa una opción: "))
	match opcion:
		case 1:
			system('clear')
			print("\033[0m---Registro estudiante---\n")
			estudiante.registro()
		case 2:
			system('clear')
			print("\033[0m---Catálogo Biblioteca (nombre)---\n")
			Biblioteca.catalogo()
		case 3:
			system('clear')
			print("\033[0m---Reserva de libros---\n")
			db.prompt_update_contact()
		case 4:
			system('clear')
			print("\033[0m---Prestamo de libros---\n")
			db.prompt_delete_contact()
		case 5:
			system('clear')
			print("\033[0m---Notificaciones---\n")
			db.prompt_delete_contact()
		case 6:
			system('clear')
			print("\033[0m---Seguimiento libros---\n")
			db.prompt_delete_contact()
		case 7:
			system('clear')
			print("\033[0m---Gestión de usuarios---\n")
			baseDatos.actualizarUsuario()
		case 8:
			system('clear')
			print("\033[0m---Sistema de multas---\n")
			db.prompt_delete_contact()
		case 9:
			system('clear')
			print("\033[0m---Servicios en línea---\n")
			db.prompt_delete_contact()
		case 10:
			system('clear')
			print("\033[0m---Registro de devolución de los libros---\n")
			db.prompt_delete_contact()
		case 11:
			system('clear')
			print("\033[0m---Generar informe de la biblioteca---\n")
			db.prompt_delete_contact()
		case 12:
			system('clear')
			print("\033[0m---Estadísticas sobre el número de visitas a la biblioteca---\n")
			db.prompt_delete_contact()
		case 13:
			system('clear')
			print("\033[0m---Estadísticas del número de libros prestados, el número de multas, etc.---\n")
			db.prompt_delete_contact()
		case 14:
			system('clear')
			print("\033[0m---Sistema de gestión de la biblioteca---\n")
			db.prompt_delete_contact()
		case 15:
			system('clear')
			print("\033[0m---Historial de préstamos---\n")
			db.prompt_delete_contact()
		case 16:
			system('clear')
			print("\033[0m---Reservas de salas de estudio---\n")
			db.prompt_delete_contact()
		case 17:
			print(f"\033[36mGracias... ¡Vuelve pronto!")
			exit()

if __name__ == "__main__":
	#Se carga la base de datos de libros
	#baseDatos.cargarDBLibros()
	#Se carga la base de datos de estudiantes
	#baseDatos.cargarDBEstudiantes()
	while True:
		#Limpiamos la pantalla
		system('clear')
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