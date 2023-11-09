compras = []

def agregar_compra(compra):
    compras.append(compra)
    print(f"La compra '{compra}' se ha agregado correctamente.")


compra1 = "Zapatos"
compra2 = "Ropa"
compra3 = "Electrodomésticos"

agregar_compra(compra1)
agregar_compra(compra2)
agregar_compra(compra3)

print("Lista de compras actual:", compras)


compras = []

def agregar_compra(nombre, monto):
    compras.append((nombre, monto))
    print(f"La compra de {nombre} por ${monto} se ha agregado correctamente.")


def mostrar_compras():
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, (nombre, monto) in enumerate(compras, 1):
            print(f"Compra {i}: {nombre} - Monto: ${monto}")


agregar_compra("Zapatos", 40)
agregar_compra("Ropa", 50)
agregar_compra("Electrodomésticos", 300)


mostrar_compras()

def mostrar_total(total):
    total_formateado = "${:,.2f}".format(total)
    print("Total gastado: " + total_formateado)


total_gastado = 1234.56
mostrar_total(total_gastado)

# Inicializamos una lista para almacenar las compras

compras = []

# Función para agregar compras a la lista
def agregar_compras():
    monto_producto = float(input("Ingrese el monto del producto: "))
    compras.append(monto_producto)
    print("Compra agregada.")

# Función para mostrar las compras
def mostrar_compras():
    print("Lista de compras:")
    for i, monto in enumerate(compras, 1):
        print(f"{i}. ${monto:.2f}")

# Función para mostrar el total gastado
def mostrar_total():
    total_gastado = sum(compras)
    print("Total gastado:")
    print("${:.2f}".format(total_gastado))

# Menú interactivo
while True:
    print("\nMenú:")
    print("1. Agregar compras")
    print("2. Mostrar compras")
    print("3. Mostrar total gastado")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_compras()
    elif opcion == '2':
        mostrar_compras()
    elif opcion == '3':
        mostrar_total()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("¡Gracias por usar el programa!")