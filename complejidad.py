import main, baseDatos
from os import system
from replit import Database

db = Database("https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzQ2MDA2NTEsImlhdCI6MTY3NDQ4OTA1MSwiZGF0YWJhc2VfaWQiOiJkZDJhOTk1OS0xYjAzLTRiNmEtODkwZS0yMzhhM2ViYWM4M2MiLCJ1c2VyIjoiRVJJQ0tQQVRSSUNJT1BBIiwic2x1ZyI6IlByb3llY3RvLTItTW9kZWxvcyJ9.B3_FtPfYaWeH5xbOMyd2PeDLqQdEtEZoP2LTlaMxos9UU8OqEAThrHT3_xa0MXoOyJv15a3aMlr0MHUbAZmsgg")

mensajePrincipal = """
----------------------------------
1 - Registrar un estudiante por carrera
2 - Catálogo: buscar y encontrar libros, revistas, tesis, etc.
3 - Reserva de libros
4 - Prestamo de libros
5.- Notificaciones
6.- Seguimiento libros
7.- Gestión de usuarios
8.- Sistema de multas
9.- Servicios en línea: permite a los usuarios buscar y reservar materiales en línea
10.- Registro de devolución de los libros
11.- Generar informe de la biblioteca
12.- Estadísticas sobre el número de visitas a la biblioteca
13.- Estadísticas del número de libros prestados, el número de multas, etc.
14.- Sistema de gestión de la biblioteca
15.- Historial de préstamos
16.- Reservas de salas de estudio
----------------------------------
"""

diccionario_datos = {
 1: ["Leonardo Morales", "Ing. Quimica"],
 2: ["Derecho Constitucional"],
 3: ["mario castro",7,1],
 4: ["mario castro",1,2],
 5: 1,
 6: 1,
 7: ["Esteban Roca","Sotfware",1],
 8: 2,
 9: ["2"],
 10: 7,
 11: 1,
 12: 1,
 13: 1,
 14: 1,
 15: "mario castro",
 16: [2,3]
}

def menuComplejidad():
	"""
  Funcion: La funcion menuComplejidad(), nos sirve para ver complejidad del software 

 Parametros: No, contiene parametros 

 Retorna: No, retorna ningun dato 
 	"""
  #limpia la pantalla 
	system("clear")
  #mensaje para que escoga el usuario si desea ver la complejidad de tiempo o espacio 
	print(
	 "\033[0m[O] Volver al menú principal \n[1] Calcular complejidad tiempo\n[2] Calcular Complejidad espacio"
	)
  #Se utiliza un bucle while para pedir al usuario que ingrese una opción (0, 1 o 2). Si el usuario ingresa algo que no es un número, se le informa que debe ingresar solo números.
	while True:
		try:
			opcion = int(input("\033[0m\nSeleccione la opción para calcular la complejidad: "))
			break
		except ValueError:
			print("\033[31mEntrada inválida, ingrese solo numeros")
  #Se utiliza una estructura de control if-elif para determinar qué acción se debe realizar según la opción elegida por el usuario:
	if opcion == 0:
    #Si la opción es 0, se llama a la función "regresarmenu" del módulo "main", lo que probablemente lleva al usuario a un menú principal.
		main.regresarmenu()
  #Si la opción es 1, se muestra al usuario el mensaje "Calculo Complejidad de Tiempo" y se pide al usuario que seleccione un proceso para calcular la complejidad de tiempo.
	elif opcion == 1:
		print("\033[0mCalculo Complejidad de Tiempo")
		print(f"\033[36m{mensajePrincipal}")
    # se utiliza un bucle while para pedir al usuario que ingrese una opción (0, 1 o 2). Si el usuario ingresa algo que no es un número, se le informa que debe ingresar solo números. Luego se obtiene el dato correspondiente en el diccionario diccionario_datos y se llama a la función "complejidad_Big_o" del módulo "baseDatos" pasando como parámetros los datos y el proceso seleccionado.
		while True:
			try:
				proceso = int(input("\033[0m\nSeleccione un proceso para calcular la complejidad de tiempo: "))
				break
			except ValueError:
				print("\033[31mEntrada inválida, ingrese solo numeros")
		datos = diccionario_datos[proceso]
		baseDatos.complejidad_Big_o(datos,proceso)
  #Si la opción es 2, se muestra al usuario el mensaje "Calculo Complejidad de Espacio" y se pide al usuario que seleccione un proceso para calcular la complejidad de espacio.
	else:
		print("\033[0mCalculo Complejidad de Espacio")
		print(f"\033[36m{mensajePrincipal}")
    # se utiliza un bucle while para pedir al usuario que ingrese una opción (0, 1 o 2). Si el usuario ingresa algo que no es un número, se le informa que debe ingresar solo números.
		while True:
			try:
				opcion = int(
				 input(
				  "\033[0m\nSeleccione un proceso para calcular la complejidad de espacio: "
				 ))
				break
			except ValueError:
				print("\033[31mEntrada inválida, ingrese solo numeros")
		datos = diccionario_datos[opcion]
		baseDatos.complejidad_Espacio(datos,opcion)
