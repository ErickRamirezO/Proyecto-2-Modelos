import baseDatos, main,re
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
	    try:
	        opcion = int(input("[0] Volver al menú\n[1] Ver lista de usuarios\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("Por favor, ingrese solo números.")
	        system("clear")
	if opcion == 0:
		main.regresarmenu()
	baseDatos.listadoEstudiantes()
	while True:
		nombre =input("\nIngrese el nombre y apellido del estudiante nuevo: ")
		if (re.match("^[a-zA-Z]*$", nombre) and 	validarNombreApellido(nombre)):
			print("\033[31mNombre inválida, ingrese nombre y apellido")
			break
		else:
			print("Por favor, ingrese solo letras.")
	carrera = input("\033[0mIngrese la carrera: ")
	print(f"\nAñadiendo al estudiante {nombre} de la carrera {carrera}")
	baseDatos.registro_estudiante(nombre,carrera)

#punto 5 
#NOTA: ARREGALR LOS COLORES
def notificacion():
	while True:
		try:
			opcion = int(input("[0] Volver al menú\n[1] Ver lista de usuarios con reserva\n[2] Ver notificacion enviadas\nIngrese una opción: "))
			break
		except ValueError:
			print("Por favor, ingrese solo números.")
			system("clear")
	if opcion == 0:
		main.regresarmenu()
	if opcion == 1:
		baseDatos.listadoEstudiantesReserva()
		while True:
			try:
				numero = int(input("\nIngrese el número del estudiante para notificarle: "))
				break
			except ValueError:
				print("Por favor, ingrese solo números.")
				system("clear")
		baseDatos.notificarUsuario(numero)
	else:
		baseDatos.listadoEstudiantesNotificados()
		

#punto 15
def historialPrestamosReservas():
	while True:
		nombre =input("\nIngrese el nombre y apellido del estudiante nuevo: ").lower()
		if (re.match("^[a-zA-Z]*$", nombre) and validarNombreApellido(nombre)):
			print("\033[31mNombre inválida, ingrese nombre y apellido")
			break
		else:
			print("Por favor, ingrese solo letras.")
	if baseDatos.obtenerEstudiante(nombre):
	    print("\033[0mEl nombre ingresado es \033[32mcorrecto")
		# Se obtiene el historial
	    baseDatos.obtenerHistorialReservasPrestamos(nombre)
	else:
	    print("\033[31mLa entrada no es válida, no se encuentra en la base de datos")
	    input("\n\033[0mPresione una tecla para continuar... ")
	    system("clear")
	    historialPrestamosReservas()
