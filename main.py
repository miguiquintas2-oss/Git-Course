def get_number(p1):
	input(p1)


def menu():
	while True:
			
		print("\nSeleccione una opción:")
		print("1 Sumar")
		print("2 Restar")
		print("3 Salir")
		choice = input("Opción: ").strip()
		if choice == '1':
			a = get_number("Ingrese el primer número: ")
			b = get_number("Ingrese el segundo número: ")
			print(f"Resultado: {a} + {b} = {a + b}")
		elif choice == '2':
			a = get_number("Ingrese el primer número: ")
			b = get_number("Ingrese el segundo número: ")
			print(f"Resultado: {a} - {b} = {a - b}")
		elif choice == '3':
			print("Saliendo.")
			break
		else:
			print("Opción no válida. Intente de nuevo.")
