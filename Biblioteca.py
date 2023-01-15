import baseDatos
from os import system
#punto 2

def catalogo():
	print("\n[1] Buscar por titulo")
	print("[2] Buscar por autor")
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	match opcion:
		case 1:
			titulo = input("Ingrese el titulo del libro: ").lower()
			baseDatos.buscarLibro(titulo)
		case 2:
			autor = input("Ingrese el autor del libro: ").lower()
			baseDatos.buscarLibro(autor)

#punto 3
def reservaLibros():
	baseDatos.obtenerLibros()
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese el número del libro a reservar: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	if baseDatos.validarEjemplarDisponible(opcion-1) == False:
		print("\033[31m El ejemplar elegido no se puede reservar porque no se encuentra disponible elija otro")
		input("\n\033[0mPresione una tecla para continuar... ")
		system("clear")
		reservaLibros()
	else:
		print("\033[32m ¡Ejemplar reservado con éxito!")
		#anadir a la base de datos la reserva que ha hecho aumentar en numero y en la lista de libros reservados de cada estudiante
		#[reserva_nombre_estudiante] = [lista con todas las reservas]
	
def ingresoDatosParaReservaLibro():
	nombre = input("\033[0mIngrese el nombre y apellido del estudiante: ").lower()
	#verificar que ingrese solo letras y se verifica en la base de datos el nombre del estudiante
	if baseDatos.obtenerEstudiante(nombre):
	    print("\033[0mEl nombre ingresado es \033[32mcorrecto")
		# Se verifica que no tenga más de 3 libros reservados
	    numero_libros_reservados = baseDatos.validarNumeroReservaLibros(nombre)
	    if numero_libros_reservados<=3: 
		    print("\033[33m Puede hacer la reserva de un libro\n")
		    reservaLibros()
	    else:
		    print("\033[31m Lo sentimos no puede hacer la reserva de su libro porque alcanzo el número máximo de reservas (3)")
	else:
	    print("\033[31mLa entrada no es válida, no se encuentra en la base de datos")
	    input("\n\033[0mPresione una tecla para continuar... ")
	    system("clear")
	    ingresoDatosParaReservaLibro()
		
	
#punto 4
def prestamoLibros():
	pass