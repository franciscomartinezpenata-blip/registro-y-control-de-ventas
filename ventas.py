def calcular_total(precio, cantidad):

    total = precio * cantidad
    return total


def guardar_venta(lista, producto, precio, cantidad, total):

    venta = [producto, precio, cantidad, total]
    lista.append(venta)


def mostrar_resumen(lista):

    print("\nRESUMEN DE VENTAS")

    total_dia = 0

    if len(lista) == 0:
        print("No se registraron ventas")

    else:

        for venta in lista:

            producto = venta[0]
            cantidad = venta[2]
            total = venta[3]

            print("\nProducto:", producto)
            print("Cantidad vendida:", cantidad)

            total_dia = total_dia + total

        print("\nTotal recaudado: $", total_dia)
