from datos import preguntar_si_no, ingresar_datos
from ventas import calcular_total, guardar_venta, mostrar_resumen


def main():

    lista_ventas = []

    continuar = preguntar_si_no("¿Quiere registrar una venta? (si/no): ")

    while continuar == "si":

        producto, precio, cantidad = ingresar_datos()

        total = calcular_total(precio, cantidad)

        print("Total de esta venta:", total)

        guardar_venta(lista_ventas, producto, precio, cantidad, total)

        continuar = preguntar_si_no("¿Desea registrar otra venta? (si/no): ")

    mostrar_resumen(lista_ventas)


main()
