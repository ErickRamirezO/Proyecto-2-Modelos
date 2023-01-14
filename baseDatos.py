from replit import Database
from memory_profiler import profile
import big_o
import datos as Datos
from os import system
db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzM4MjAyNjYsImlhdCI6MTY3MzcwODY2NiwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.yvV7rTJBFyQ3focAr8tK0p1X7gLS85o6K04J_saXfpqUaXV7h4e0s5gq_Zc78PstwEhnUxCBDauGw5_tpp4cew")

#usar diccionario revistas = {1,2,3,...,n}
def cargarDBLibros():
	print("Cargando base de datos libros...")
	db["Titulos_libros"]=db["Autores_libros"]=db["Disponibilidad"]=[]
	for i in range(len(Datos.titulos)):
		db["Titulos_libros"].append(Datos.titulos[i])
		db["Autores_libros"].append(Datos.autores[i])
		db["Disponibilidad"].append(Datos.disponibilidad[i])
	print("\033[32mLibros cargados exitosamente")
		
def cargarDBEstudiantes():
	print("Cargando base de datos de estudiantes...")
		#diccionario estudiantes
	db["Estudiantes"]=db["Carrera_estudiantes"]=[]
	for i in range(len(Datos.estudiantes)):
		db["Estudiantes"].append(Datos.estudiantes[i])
		db["Carrera_estudiantes"].append(Datos.carrera[i])
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
		return '\033[32mEstudiante registrado exitosamente'

#punto 7
def actualizarUsuario():
	print("Estudiantes ingresados")
	print("----------------------")
	print("\033[33m\tEstudiante\t\t\t\tCarrera ")
	for i in range(len(db["Estudiantes"])):
		print(f"""\033[0m{i+1}) {db["Estudiantes"][i]} \t\t\t {db["Carrera_estudiantes"][i]}""")
	num_est = int(input("\n\033[36mIngrese el número de estudiante a actualizar los datos: "))
	nuevo_nombre = input("Ingrese nombre y apellido del estudiante: ")
	nueva_carrera = input("Ingrese la carrera del estudiante: ")
	db["Estudiantes"][num_est-1] = nuevo_nombre
	db["Carrera_estudiantes"][num_est-1] = nueva_carrera
	system("clear")
	print("\033[0mInformación actualizada del usuario")
	for i in range(len(db["Estudiantes"])):
		if db["Estudiantes"][i] == nuevo_nombre and db["Carrera_estudiantes"][i] == nueva_carrera:
			print(f"""\033[32m--> {i+1}) Estudiante: {nuevo_nombre} \t\t\t {nueva_carrera}""")
		else:
			print(f"""\033[0m{i+1}) Estudiante: {db["Estudiantes"][i]} \t\t\t {db["Carrera_estudiantes"][i]}""")


def get_contact(name):
    number = db.get(name)
    return number

def search_contacts(search):
    match_keys = db.prefix(search)
    return {k: db[k] for k in match_keys}

def update_number(old_name, new_number):
    db[old_name] = new_number

def update_contact(old_name, new_name, new_number):
    db[new_name] = new_number
    del db[old_name]

def delete_contact(name):
    del db[name]


