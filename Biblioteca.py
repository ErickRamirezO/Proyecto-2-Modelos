import baseDatos,main,estudiante
from os import system

#punto 2
def catalogo():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	print("\n[1] Buscar por titulo\n[2] Buscar por autor\n[0] Volver al menú")
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        if opcion ==0:
		        main.regresarmenu()
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
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	baseDatos.obtenerLibros()
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese el número del libro a reservar: "))
	        if opcion == 0:
	            main.regresarmenu()
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
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	baseDatos.listadoEstudiantes()
	nombre = input("\033[0m> Para volver al menú digite [0]\nIngrese el nombre y apellido del estudiante: ").lower()
	if int(nombre) == 0:
		main.regresarmenu()
	#verificar que ingrese solo letras y se verifica en la base de datos el nombre del estudiante
	if baseDatos.validarEstudiante(nombre):
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


#punto 8
def sistemaMultas():
	pass

#punto 9
def serviciosEnLinea():
	pass
		
#punto10
def registroDevolucionLibros():
	"""
  Funcion:

 Parametros:

 Retorna:
 	"""
	print("\n[0] Volver al menú\n[1] Mostrar listado estudiantes\n")
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	if opcion ==0:
		main.regresarmenu()
	else:
		baseDatos.listadoEstudiantes()
		while True:
		    try:
		        numero_estudiante = int(input("\033[0m\nIngrese el numero del estudiante: "))
		        break
		    except ValueError:
		        print("\033[31mEntrada inválida, ingrese solo numeros")

		if baseDatos.registroDevolucionLibros(numero_estudiante):
			print("El registro de devolucion del libro fue realizado con éxito")
		else:
			print("El alumno no tiene un préstamo activo")
		

def generarInforme():
	print("\n[0] Volver al menú\n[1] Generar informe\n")
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	if opcion ==0:
		main.regresarmenu()
	else:
		baseDatos.mostrarInforme()

#punto 14
def gestionBiblioteca():
	pass
		
#16 salas de estudio
def reservaSala():
	"""
 
 	"""
	print("\n[0] Volver al menú\n[1] Mostrar salas\n")
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	if opcion ==0:
		main.regresarmenu()
	else:
		baseDatos.mostrarSalas()
		print("\n\n[0] Volver\n[1] Reservar sala\n")
		while True:
		    try:
		        opcion = int(input("\033[0m\nIngrese una opción: "))
		        break
		    except ValueError:
		        print("\033[31mEntrada inválida, ingrese solo numeros")
		if opcion ==0:
			main.regresarmenu()
		else:
			system("clear")
			baseDatos.mostrarSalas()
			baseDatos.listadoEstudiantes()
			while True:
			    try:
				    numero_sala = int(input("\033[0m\nIngrese el numero de sala: "))
				    numero_estudiante = int(input("\nIngrese el numero del estudiante: "))
				    break
			    except ValueError:
				        print("\033[31mEntrada inválida, ingrese solo numeros")
			if baseDatos.disponibilidadSala(numero_sala,numero_estudiante):
				print("Reserva de la sala fue realizada con éxito")
			else:
				print("No se puede reservar esa sala porque no está disponible!")