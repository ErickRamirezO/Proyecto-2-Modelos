import baseDatos 
from os import system
#validacion nombre y apellido
def validarNombreApellido(text):
	nombre = text.split()
	if len(nombre) == 2:
		return True
	else:
		return False

#punto 1 
	#Usar función split para validar qhe ingrese nombre y apellido 
def registro():
	while True:
		nombre = input("Ingrese el nombre del estudiante: ")
		if validarNombreApellido(nombre):
			print("\033[32mNombre válido")
		break
	else:
		print("\033[31mNombre inválida, ingrese nombre y apellido")
	carrera = input("\033[0mIngrese la carrera: ")
	if not nombre or not carrera:
		return "\033[31mTodos los campos deben estar completos."
	if not isinstance(nombre, str):
		return "\033[31mEl nombre debe ser una cadena de caracteres"
	print(f"\nAñadiendo al estudiante {nombre} de la carrera {carrera}")
	baseDatos.registro_estudiante(nombre,carrera)

#punto 5
def notificacion():
	pass


#punto 15
def historialPrestamosReservas():
	nombre = input("\033[0mIngrese el nombre y apellido del estudiante: ").lower()
	#verificar que ingrese solo letras y se verifica en la base de datos el nombre del estudiante
	if baseDatos.obtenerEstudiante(nombre):
	    print("\033[0mEl nombre ingresado es \033[32mcorrecto")
		# Se obtiene el historial
	    baseDatos.obtenerHistorialReservasPrestamos(nombre)
	else:
	    print("\033[31mLa entrada no es válida, no se encuentra en la base de datos")
	    input("\n\033[0mPresione una tecla para continuar... ")
	    system("clear")
	    historialPrestamosReservas()
