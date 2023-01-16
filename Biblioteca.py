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
			titulo = input("\033[0mIngrese el titulo del libro: ").lower()
			if baseDatos.validarbusquedaLibro(titulo):
				baseDatos.buscarLibro(titulo)
			else:
				print("\033[31mLo sentimos no hubo éxito en su búsqueda por titulo...")
		case 2:
			autor = input("\033[0mIngrese el autor del libro: ").lower()
			if baseDatos.validarbusquedaLibro(autor):
				baseDatos.buscarLibro(autor)
			else:
				print("\033[31mLo sentimos no hubo éxito en su búsqueda por autor...")

#punto 3
def reservaLibros(nombre,reserva_o_prestamos):
	baseDatos.obtenerLibros()
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese el número del libro a reservar: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	if baseDatos.validarEjemplarDisponible(opcion-1) == False:
		print("\033[31m El ejemplar elegido no se puede reservar o prestar porque no se encuentra disponible elija otro")
		input("\n\033[0mPresione una tecla para continuar... ")
		system("clear")
		reservaLibros(nombre)
	else:
		baseDatos.actualizarLibrosReservados(nombre,opcion-1,reserva_o_prestamos)
	
def ingresoDatosParaReservaOPrestamoLibro(reserva_o_prestamos):
	nombre = input("\033[0mIngrese el nombre y apellido del estudiante: ").lower()
	#verificar que ingrese solo letras y se verifica en la base de datos el nombre del estudiante
	if baseDatos.obtenerEstudiante(nombre):
	    print("\033[0mEl nombre ingresado es \033[32mcorrecto")
		# Se verifica que no tenga más de 3 libros reservados
	    if baseDatos.validarNumeroReservaLibros(nombre)<3: 
		    print("\033[33m Puede hacer la reserva de un libro\n")
		    input("\n\033[0mPresione una tecla para continuar... ")
		    system("clear")
		    reservaLibros(nombre,reserva_o_prestamos)
	    else:
		    print("\033[31m Lo sentimos no puede hacer la reserva de un libro porque alcanzo el número máximo de reservas (3)")
	else:
	    print("\033[31mLa entrada no es válida, no se encuentra en la base de datos")
	    input("\n\033[0mPresione una tecla para continuar... ")
	    system("clear")
	    ingresoDatosParaReservaOPrestamoLibro(reserva_o_prestamos)
		
