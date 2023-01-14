import baseDatos 

#validacion nombre y apellido
def validarNombreApellido(text):
	nombre = text.split()
	if len(nombre) == 2:
		return True
	else:
		return False

#punto 1
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
		
