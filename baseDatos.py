from replit import Database
from memory_profiler import profile
import big_o
import datos as Datos
from os import system
db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzM4MjAyNjYsImlhdCI6MTY3MzcwODY2NiwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.yvV7rTJBFyQ3focAr8tK0p1X7gLS85o6K04J_saXfpqUaXV7h4e0s5gq_Zc78PstwEhnUxCBDauGw5_tpp4cew")


def cargarDBLibros():
	print("Cargando base de datos libros...")
	db["Titulos_libros"]=db["Autores_libros"]=db["Disponibilidad"]=db["Copias_disponibles"]=db["Ubicacion"]=db["Conservacion"]=[]
	for i in range(len(Datos.titulos)):
		db["Titulos_libros"].append(Datos.titulos[i])
		db["Autores_libros"].append(Datos.autores[i])
		db["Disponibilidad"].append(Datos.disponibilidad[i])
		db["Copias_disponibles"].append(Datos.copias_disponibles[i])
		db["Ubicacion"].append(Datos.ubicacion[i])
		db["Conservacion"].append(Datos.conservacion[i])
	print("\033[32mLibros cargados exitosamente")
		
def cargarDBEstudiantes():
	print("Cargando base de datos de estudiantes...")
		#diccionario estudiantes
	db["Estudiantes"]=db["Carrera_estudiantes"]=db["Numero_libros_reservados"]=db["Numero_libros_prestados"]=[]
	for i in range(len(Datos.estudiantes)):
		db["Estudiantes"].append(Datos.estudiantes[i])
		db["Carrera_estudiantes"].append(Datos.carrera[i])
		db["Numero_libros_reservados"].append(Datos.numero_libros_reservados[i])
		db["Numero_libros_prestados"].append(Datos.numero_libros_prestados[i])
	print("\033[32mEstudiantes cargados exitosamente")
	
@profile
def registro_estudiante(nombre,carrera):
	for i in range(len(db["Estudiantes"])):
		if str(nombre) in db["Estudiantes"][i]:
			print("\033[31mEl nombre ingresado ya existe")
	else:
		# Agregar el nuevo estudiante a la base de datos de replit
		db["Estudiantes"].append(nombre)
		db["Carrera_estudiantes"].append(carrera)
		db["Numero_libros_reservados"].append(0)
		return '\033[32mEstudiante registrado exitosamente'
		
#punto 3 y 4
def obtenerLibros():
	print("\033[0m{:^8}\033[33m{:^40}\033[36m{:^28}\033[32m{:^14}".format("Número","Libros","Autor","Disponibilidad"))
	for i in range(len(db["Titulos_libros"])):
		print("\033[0m{:^8}{:^40}{:^28}{:^14}".format(i+1,db["Titulos_libros"][i],db["Autores_libros"][i],db["Disponibilidad"][i]))

def validarEjemplarDisponible(i):
	if db["Disponibilidad"][i] == "Si":
		return True
	return False

def obtenerEstudiante(nombre_estudiante):
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i].lower() == nombre_estudiante:
			return True
	return False

def validarNumeroReservaLibros(nombre_estudiante):
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i].lower() == nombre_estudiante:
			return db["Numero_libros_reservados"][i]

def actualizarLibrosReservados(nombre_estudiante,numeroLibroReservar,reserva_o_prestamo):
	db["Libros_reservados_"+nombre_estudiante] = []
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i].lower() == nombre_estudiante:
			#1 para reserva y 2 para prestamo
			if reserva_o_prestamo == 1:
				db["Numero_libros_reservados"][i] = db["Numero_libros_reservados"][i] + 1
				db["Libros_reservados_"+nombre_estudiante].append(db["Titulos_libros"][numeroLibroReservar])
				print("\033[32m ¡Ejemplar reservado con éxito!")
			else:
				db["Libros_prestados_"+nombre_estudiante].append(db["Titulos_libros"][numeroLibroReservar])
				print("\033[32m ¡Ejemplar prestado con éxito!")
#fin punto 3 y 4
			
#punto 6
def seguimientoLibros():
	print("\033[33m{:^40}{:^28}{:^14}{:^18}{:^40}{:^14}".format("Libros","Autor","Disponibilidad","Número de copias","Ubicacion","Conservación"))
	for i in range(len(db["Titulos_libros"])):
		print("\033[0m{:^40}{:^28}{:^14}{:^18}{:^40}{:^9}".format(db["Titulos_libros"][i],db["Autores_libros"][i],db["Disponibilidad"][i],db["Copias_disponibles"][i],db["Ubicacion"][i],db["Conservacion"][i]))

def buscarLibro(libro):
	for i in range(len(db["Titulos_libros"])):
		if db["Titulos_libros"][i].lower() == libro or db["Autores_libros"][i].lower() == libro:
			print(f"""\n\033[0m Se encontró el siguiente libro\n\n\033[33m{db["Titulos_libros"][i]} de {db["Autores_libros"][i]}""")
			print(f"""\033[0mDisponible: \033[36m{db["Disponibilidad"][i]}""")
	else:
		print("\033[31mNo se encontró ningún libro con ese titulo o autor ingresado")

#punto 7
def actualizarUsuario():
	print("Estudiantes ingresados")
	print("----------------------")
	print("\033[0m{:^8}\033[33m{:^20}\033[32m{:^25}".format("Número","Estudiante","Carrera"))
	for i in range(len(db["Estudiantes"])):
		print("\033[0m{:^8}{:^20}{:^25}".format(i+1,db["Estudiantes"][i],db["Carrera_estudiantes"][i]))
	num_est = int(input("\033[36mIngrese el número de estudiante a actualizar los datos: "))
	nuevo_nombre = input("Ingrese nombre y apellido del estudiante: ")
	nueva_carrera = input("Ingrese la carrera del estudiante: ")
	db["Estudiantes"][num_est-1] = nuevo_nombre
	db["Carrera_estudiantes"][num_est-1] = nueva_carrera
	system("clear")
	print("\033[0mInformación actualizada del usuario")
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i] == nuevo_nombre and db["Carrera_estudiantes"][i] == nueva_carrera:
			print("\033[32m{:^8}{:^20}{:^25}".format(i+1,nuevo_nombre,nueva_carrera))
		else:
			print("\033[0m{:^8}{:^20}{:^25}".format(i+1,db["Estudiantes"][i],db["Carrera_estudiantes"][i]))

	