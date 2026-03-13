def preguntar_si_no(mensaje):

    respuesta = input(mensaje).strip().lower()

    while respuesta != "si" and respuesta != "no":
        print("Entrada inválida. Responda solo con 'si' o 'no'.")
        respuesta = input(mensaje).strip().lower()

    return respuesta


def ingresar_datos():

    producto = input("Ingrese el nombre del producto: ").strip()

    precio_valido = False

    while precio_valido == False:

        precio_input = input("Ingrese el precio: ").replace(",", ".").strip()

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
            cantidad = int(input("Ingrese la cantidad: ").strip())

            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                cantidad_valida = True

        except ValueError:
            print("Debe ingresar un número entero.")

    return producto, precio, cantidad