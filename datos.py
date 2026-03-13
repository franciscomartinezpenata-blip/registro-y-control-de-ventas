def preguntar_si_no(mensaje):

    respuesta = input(mensaje).lower()

    while respuesta != "si" and respuesta != "no":
        print("Entrada inválida. Responda solo con 'si' o 'no'.")
        respuesta = input(mensaje).lower()

    return respuesta


def ingresar_datos():

    producto = input("Ingrese el nombre del producto: ")

    precio_valido = False

    while precio_valido == False:

        precio_input = input("Ingrese el precio: ")
        precio_input = precio_input.replace(",", ".")

        try:
            precio = float(precio_input)

            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                precio_valido = True

        except ValueError:
            print("Debe ingresar un número válido.")

    cantidad_valida = False

    while cantidad_valida == False:

        try:
            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                cantidad_valida = True

        except ValueError:
            print("Debe ingresar un número entero.")

    return producto, precio, cantidad