import baseDatos, main, re
from os import system


#validacion nombre y apellido
def validarNombreApellido(texto):
	"""
  Funcion: La función "validarNombreApellido(texto)" valida si un texto dado contiene solo un nombre y un apellido, retornando verdadero si es así, o falso en caso contrario.

 Parametros: texto

 Retorna: retorna verdadero o falso 
 	"""
  #Se utiliza el método "split()" para dividir la cadena "texto" en una lista de palabras utilizando el espacio como separador.
	nombre = texto.split()
  #Se verifica si la longitud de la lista es igual a 2, lo que indicaría que tiene 2 elementos, un nombre y un apellido.
	if len(nombre) == 2:
    #Si la longitud de la lista es igual a 2, se retorna verdadero, lo que significa que el nombre y apellido son válidos.
		return True
    #caso contrario 
	else:
    #Si la longitud de la lista es diferente de 2, se retorna falso, lo que significa que el nombre y apellido no son válidos.
		return False


#punto 1
#Usar función split para validar qhe ingrese nombre y apellido
def registro():
	"""
  Funcion: La función "registro()" permite al usuario registrar un nuevo estudiante en la base de datos, validando que los datos ingresados sean correctos.

 Parametros: No, contiene parametros

 Retorna: No, retorna ningun valor 
 	"""
  #Se declara una lista vacía llamada "lista".
	lista=[]
  #Se utiliza un bucle while para asegurar que el valor ingresado para la variable "opcion" sea un número entero. En caso de que no sea un número, se imprime un mensaje de error.
	while True:
		try:
			opcion = int(
			 input(
			  "[0] Volver al menú\n[1] Ver lista de usuarios\nIngrese una opción: "))
			break
		except ValueError:
			print("Por favor, ingrese solo números.")
      #limpia la pantalla 
			system("clear")
  #Si la opción seleccionada es 0, se regresa al menú principal.
	if opcion == 0:
		main.regresarmenu()
  #Si la opción seleccionada es 1, se llama a la función "listadoEstudiantes()" de la base de datos, la cual probablemente muestra una lista de estudiantes registrados.
	baseDatos.listadoEstudiantes()
  #Se utiliza un bucle while para pedir al usuario que ingrese el nombre y apellido del estudiante nuevo, y se valida si los datos ingresados son correctos mediante la función "validarNombreApellido(nombre)"
	while True:
		nombre = input(
		 "\n\033[0mIngrese el nombre y apellido del estudiante nuevo: ")
    #Si los datos ingresados son correctos, se imprime un mensaje de confirmación y se rompe el bucle. Si los datos son incorrectos, se imprime un mensaje de error y se vuelve a pedir al usuario que ingrese los datos.
		if (validarNombreApellido(nombre)):
			print("\033[32mDatos correctos")
			break
    #Se pide al usuario que ingrese la carrera del estudiante nuevo y se imprime un mensaje confirmando los datos ingresados.
		else:
			print("\033[31mNombre inválida, ingrese nombre y apellido")
	carrera = input("\033[0mIngrese la carrera: ")
	print(f"\nAñadiendo al estudiante {nombre} de la carrera {carrera}")
  #Se añade el nombre y la carrera del estudiante nuevo a la lista "lista".
	lista.append(nombre)
	lista.append(carrera)
  #Se llama a la función "registro_estudiante(lista)" de la base de datos, la cual probablemente agrega al estudiante nuevo a la base de datos.
	baseDatos.registro_estudiante(lista)


#punto 5
def notificacion():
	"""
  Funcion: La funcion notificacion, notifica al estudiante que estan en las listas 

 Parametros: No, contiene ningun parametro 

 Retorna: No, retorna ningun dato 
 
 	"""
  #Se utiliza un bucle while para pedir al usuario que ingrese una opción (0, 1 o 2). Si el usuario ingresa algo que no es un número, se le informa que debe ingresar solo números.
	while True:
		try:
      #mensaje para que ingrese la opcion que desee 
			opcion = int(
			 input(
			  "[0] Volver al menú\n[1] Ver lista de usuarios con reserva\n[2] Ver notificacion enviadas\nIngrese una opción: "
			 ))
			break
    #en caso de no ingresar bien 
		except ValueError:
      #mensaje que ingrese solo numeros 
			print("Por favor, ingrese solo números.")
      #limpia la pantalla 
			system("clear")
  #Se utiliza una estructura de control if para determinar qué acción se debe realizar según la opción elegida por el usuario:
	if opcion == 0:
    #Si la opción es 0, se llama a la función "regresarmenu" del módulo "main", lo que probablemente lleva al usuario a un menú principal.
		main.regresarmenu()
  #Si la opción es 1, se llama a la función "listadoEstudiantesReserva" del módulo "baseDatos" para mostrar una lista de estudiantes con reserva, luego se pide al usuario que ingrese el número de un estudiante de esa lista para notificarle. Luego se llama a la función "notificarUsuario" del módulo "baseDatos" pasando como parámetro el número ingresado.
	if opcion == 1:
		baseDatos.listadoEstudiantesReserva()
		while True:
			try:
        #ingrese un numero que sea entero 
				numero = int(
				 input("\nIngrese el número del estudiante para notificarle: "))
				break
      #caso contrario de no ingresar bien el numero 
			except ValueError:
        #mensaje que vuelva a ingresar la opcion 
				print("Por favor, ingrese solo números.")
        #limpia la pantalla 
				system("clear")
		baseDatos.notificarUsuario(numero)
  #Si la opción es 2, se llama a la función "listadoEstudiantesNotificados" del módulo "baseDatos" para mostrar una lista de estudiantes a los que se les ha enviado notificaciones.
	else:
		baseDatos.listadoEstudiantesNotificados()


#punto 15
def   historialPrestamosReservas():
	"""
  Funcion: La funcion "historialPrestamosReservas()" nos muestra el historial de todos los usuarios registrados en la biblioteca 

 Parametros: No, contiene ningun parametro 

 Retorna: No, retorna ningun dato 
 	"""
  #Se utiliza un bucle while para pedir al usuario que ingrese el nombre y apellido del estudiante del cual se quiere ver el historial de préstamos y reservas.
	while True:
		nombre = input(
		 "\nIngrese el nombre y apellido del estudiante nuevo: ").lower()
    #Se utiliza la función "re.match" para verificar que el nombre ingresado contiene solo letras y luego se utiliza la función "validarNombreApellido" para validar que el nombre y apellido sean correctos. 
		if (re.match("^[a-zA-Z]*$", nombre) and validarNombreApellido(nombre)):
			print("\033[31mNombre inválida, ingrese nombre y apellido")
			break
    #Si no es así, se informa al usuario y se sale del bucle.
		else:
			print("Por favor, ingrese solo letras.")
  #Se utiliza una estructura de control if para determinar si el nombre ingresado existe en la base de datos. Si es así, se llama a la función "obtenerHistorialReservasPrestamos" del módulo "baseDatos" 
	if baseDatos.obtenerEstudiante(nombre):
		print("\033[0mEl nombre ingresado es \033[32mcorrecto")
		# Se obtiene el historial
		baseDatos.obtenerHistorialReservasPrestamos(nombre)
  #Si no es así, se informa al usuario que la entrada no es válida y se llama de nuevo a la función "historialPrestamosReservas".
	else:
		print("\033[31mLa entrada no es válida, no se encuentra en la base de datos")
    #mensaje de que presione tecla para continuar 
		input("\n\033[0mPresione una tecla para continuar... ")
    #limpia la pantalla
		system("clear")
		historialPrestamosReservas()
