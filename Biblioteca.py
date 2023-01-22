import baseDatos,main
from os import system

#punto 2
def catalogo():
	"""
  Funcion: La función primero imprime un menú de opciones para que el usuario elija, que incluye buscar un libro por título o por autor.

 Parametros: No, contiene parametros

 Retorna: No, retorna ningun valor o dato
 	"""
  #mensaje de buscar el lubro ya sea por titulo o autor
	print("\n[1] Buscar por titulo\n[2] Buscar por autor\n[0] Volver al menú")
  #se valida la entrada para asegurar que sea un número.
	while True:
	    try:
        #Si la entrada no es un número, se muestra un mensaje de error.
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        if opcion ==0:
            #nos retorna al main 
		        main.regresarmenu()
	        break
        #mensaje de error 
	    except ValueError:
        # no pide que ingresemos un numero 
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	match opcion:
  #caso numero 1
		case 1:
      #mensaje de ingreso del titulo del libro
			titulo = input("\033[0mIngrese el titulo del libro: ").lower()
      #busca en la base de datos el libro 
			if baseDatos.validarbusquedaLibro(titulo):
        #encuentra el libro 
				baseDatos.buscarLibro(titulo)
        #si el libro ingresado no esta en la base de datos le saldra un mensaje al usuario 
			else:
        #mensaje de que no se encontro ese libro 
				print("\033[31mLo sentimos no hubo éxito en su búsqueda por titulo...")
    #caso numero 2
		case 2:
      #se puede buscar el libro por autor, entonces aqui nos pide que ingresemos el nombre del autor del librp
			autor = input("\033[0mIngrese el autor del libro: ").lower()
      #si el autor esta en la base de datos se mostrara
			if baseDatos.validarbusquedaLibro(autor):
        #aqui se muestra el libro del autor 
				baseDatos.buscarLibro(autor)
      # caso contrario 
			else:
        # se imprime un mensaje de que no se encontro al autor 
				print("\033[31mLo sentimos no hubo éxito en su búsqueda por autor...")


def reservaLibros(nombre,reserva_o_prestamos):
	"""
  Funcion: La función permite al usuario reservar un libro de una lista presentada previamente, validando que el libro elegido está disponible y actualizando la base de datos con la información de la reserva del usuario.

 Parametros: nombre, reserva_o_prestamos 

 Retorna: No, retorna ningun dato 
 	"""
	lista = []
  #Se llama al método "obtenerLibros" en el objeto "baseDatos" para mostrar una lista de libros.
	baseDatos.obtenerLibros()
  #La entrada es validada para asegurar que es un número. Si la entrada no es un número, se muestra un mensaje de error.
	while True:
	    try:
        #mensaje de ingreso del numero de libros que desee reservar el usuario 
	        opcion = int(input("\033[0m\nIngrese el número del libro a reservar: "))
        # si el numero es igual a 0 nos va a regresar al menu
	        if opcion == 0:
            #aqui se regresa al menu ya que ingreso 0
	            main.regresarmenu()
            #cerramos el ciclo
	        break
        #evalua el erro 
	    except ValueError:
        # mensaje de que solo se permiten ingresar numeros 
	        print("\033[31mEntrada inválida, ingrese solo numeros")
  #Si el método devuelve false, significa que el libro no está disponible, el usuario es informado con un mensaje de error.
	if baseDatos.validarEjemplarDisponible(opcion-1) == False:
		print("\033[31m El ejemplar elegido no se puede reservar o prestar porque no se encuentra disponible elija otro")
		input("\n\033[0mPresione una tecla para continuar... ")
		system("clear")
		reservaLibros(nombre)
  #En caso contrario, la función llama al método "actualizarLibrosReservados" en el objeto "baseDatos", pasando el nombre del usuario, la elección del usuario menos uno y el parámetro "reserva_o_prestamos"
	else:
		lista.append(nombre)
		lista.append(opcion-1)
		lista.append(reserva_o_prestamos)
		baseDatos.actualizarLibrosReservados(lista)
	
def ingresoDatosParaReservaOPrestamoLibro(reserva_o_prestamos):
	"""
  Funcion: Lafuncion nos sirve para hacer la reserva o prestamos de un libro 

 Parametros: reserva_o_prestamos

 Retorna:No, retorna ningun dato 
 	"""
  #Se llama al método "listadoEstudiantes" en el objeto "baseDatos" para mostrar una lista de estudiantes.
	baseDatos.listadoEstudiantes()
  #El usuario es solicitado a ingresar el nombre y apellido del estudiante para hacer la reserva o préstamo del libro.
	nombre = input("\033[0m> Para volver al menú digite [0]\nIngrese el nombre y apellido del estudiante: ").lower()
  #Si el usuario ingresa 0, se llama a la función "main.regresarmenu()" para regresar al menú principal.
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
      #Si el estudiante tiene más de 3 libros reservados, se muestra un mensaje de error indicando que ya alcanzó el número máximo de reservas.
	    else:
		    print("\033[31m Lo sentimos no puede hacer la reserva de un libro porque alcanzo el número máximo de reservas (3)")
  #Si el nombre del estudiante ingresado no es válido, se muestra un mensaje de error indicando que la entrada no es válida y no se encuentra en la base de datos
	else:
    #mensaje de que no es valido lo ingresado 
	    print("\033[31mLa entrada no es válida, no se encuentra en la base de datos")
    #mensaje de que presione una tecla para continuar con el prestamo de libro 
	    input("\n\033[0mPresione una tecla para continuar... ")
    #limpiamos la pantalla 
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
  Funcion: La función "registroDevolucionLibros()" permite al usuario seleccionar un estudiante de una lista de estudiantes registrados y registrar la devolución de un libro prestado por ese estudiante.

 Parametros: No, contiene parametros 

 Retorna: No, retorna ningun valor 
 	"""
  #Se imprime un menú con las opciones "Volver al menú" y "Mostrar listado estudiantes"
	print("\n[0] Volver al menú\n[1] Mostrar listado estudiantes\n")
  #Se utiliza un bucle while para asegurar que el valor ingresado para la variable "opcion" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
	while True:
	    try:
          #mensaje de ingreso de opcion 
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
        #mensaje de valor incorrecto 
	        print("\033[31mEntrada inválida, ingrese solo numeros")
  #Si la opción seleccionada es 0, se regresa al menú principal.
	if opcion ==0:
		main.regresarmenu()
	else:
		baseDatos.listadoEstudiantes()
    #Si la opción seleccionada es 1, se muestra el listado de estudiantes y se utiliza un bucle while para asegurar que el valor ingresado para la variable "numero_estudiante" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
		while True:
		    try:
          #mensaje de ingreso del numero del estudiante 
		        numero_estudiante = int(input("\033[0m\nIngrese el numero del estudiante: "))
		        break
		    except ValueError:
          #opcion invalidad y sale un mensaje de que lo que ingreso es invalido y que vuelva aingresarn 
		        print("\033[31mEntrada inválida, ingrese solo numeros")
    #Si la función "registroDevolucionLibros" retorna true, significa que se ha realizado el registro de devolución del libro del estudiante especificado con éxito.
		if baseDatos.registroDevolucionLibros(numero_estudiante):
			print("El registro de devolucion del libro fue realizado con éxito")
  #caso contrario el alumno no tiene algun prestamo activo en la biblioteca 
		else:
			print("El alumno no tiene un préstamo activo")
		

def generarInforme():
	"""
 Funcion: La función "generarInforme()" permite al usuario generar un informe con estadisticas sobre los libros prestados y devueltos.

 Parametros: No, contiene parametros

 Retorna: No, retorna ningun dato 
 	
 	"""
  #Se imprime un menú con las opciones "Volver al menú" y "Generar informe"
	print("\n[0] Volver al menú\n[1] Generar informe\n")
  #Se utiliza un bucle while para asegurar que el valor ingresado para la variable "opcion" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
  #Si la opción seleccionada es 0, se regresa al menú principal.
	if opcion ==0:
		main.regresarmenu()
  #Si la opción seleccionada es 1, se llama a la función "mostrarInforme()" de la base de datos, la cual genera un informe con datos estadísticos sobre los libros prestados y devueltos en la biblioteca.
	else:
		baseDatos.mostrarInforme()

#punto 14
def gestionDePersonal():
  
	  #Se imprime un menú con las opciones "Volver al menú", "Información del personal"
	#y "Seguimiento Horas Trabajadas"
	print("\n[0] Volver al menú\n[1] Información del personal\n[2] Seguimiento horas trabajadas")
  #Se utiliza un bucle while para asegurar que el valor ingresado para la variable "opcion" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
	#Si la opción seleccionada es 0, se regresa al menú principal.
	if opcion ==0:
		main.regresarmenu()
	#Si la opción seleccionada es 1, se llama a la función "informacionDelPersonal()" de la base de datos, la cual mostrará una tabla con los datos de cada personal de la biblioteca.
	elif opcion ==1:
		baseDatos.informacionDelPersonal()
	#Si la opción seleccionada es 2 se llama a la función "informacionDelPersonal()" de la base de datos, la cual mostrará una tabla con los datos de cada personal de la biblioteca.
	else:
		baseDatos.seguimientoHorasTrabajadasPersonal()
		
#16 salas de estudio
def reservaSala():
	"""
 Funcion: La función "reservaSala()" permite al usuario ver las salas disponibles y hacer una reserva de una sala específica, si esta está disponible.

 Parametro: No, contiene ningun parametro 

 Retorna: No, retorna ningun dato 
 	"""
  #Se imprime un menú con las opciones "Volver al menú" y "Mostrar salas"
	print("\n[0] Volver al menú\n[1] Mostrar salas\n")
  #Se utiliza un bucle while para asegurar que el valor ingresado para la variable "opcion" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
	while True:
	    try:
	        opcion = int(input("\033[0m\nIngrese una opción: "))
	        break
	    except ValueError:
	        print("\033[31mEntrada inválida, ingrese solo numeros")
  #Si la opción seleccionada es 0, se regresa al menú principal.
	if opcion ==0:
		main.regresarmenu()
  #Si la opción seleccionada es 1, se llama a la función "mostrarSalas()" de la base de datos, la cual probablemente muestra una lista de salas disponibles en la biblioteca.
	else:
    #Si la opción seleccionada es 1, se llama a la función "mostrarSalas()" de la base de datos, la cual probablemente muestra una lista de salas disponibles en la biblioteca.
		baseDatos.mostrarSalas()
		print("\n\n[0] Volver\n[1] Reservar sala\n")
    #Se utiliza un bucle while para asegurar que el valor ingresado para la variable "opcion" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
		while True:
		    try:
		        opcion = int(input("\033[0m\nIngrese una opción: "))
		        break
		    except ValueError:
		        print("\033[31mEntrada inválida, ingrese solo numeros")
    #Si la opción seleccionada es 0, se regresa al menú principal.
		if opcion ==0:
			main.regresarmenu()
    #Si la opción seleccionada es 1, se llama a la función "mostrarSalas()" de la base de datos nuevamente, la cual probablemente muestra una lista de salas disponibles en la biblioteca.
		else:
      #limpia la pantalla 
			system("clear")
      #Se llama a la función "listadoEstudiantes()" de la base de datos, la cual probablemente muestra una lista de estudiantes registrados.
			baseDatos.mostrarSalas()
			baseDatos.listadoEstudiantes()
      #Se utiliza un bucle while para asegurar que el valor ingresado para las variables "numero_sala" y "numero_estudiante" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
			while True:
			    try:
            #mensaje para que ingrese el numero de la sala 
				    numero_sala = int(input("\033[0m\nIngrese el numero de sala: "))
            #ingresa el numero del estudiantes 
				    numero_estudiante = int(input("\nIngrese el numero del estudiante: "))
				    break
			    except ValueError:
            #en caso de no ingresar bien, saldra un mensaje de error que ingrese solo numero 
				        print("\033[31mEntrada inválida, ingrese solo numeros")
      #Si la función "disponibilidadSala" retorna true, significa que se ha reservado la sala con éxito.
			if baseDatos.disponibilidadSala(numero_sala,numero_estudiante):
				print("Reserva de la sala fue realizada con éxito")
      #Si la función "disponibilidadSala" retorna false, significa que la sala no está disponible para ser reservada, y se imprime un mensaje indicando que no se puede reservar la sala.
			else:
				print("No se puede reservar esa sala porque no está disponible!")