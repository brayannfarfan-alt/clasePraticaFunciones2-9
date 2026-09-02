

productos = []


def agregar_producto():

    try:
        nombre = input("Nombre del producto : \n").strip()
        
        if not nombre:
            print("Error: El nombre no debe estar vacio.")
            return

        precio = float(input("Precio: \n"))
        cantidad = int(input("Cantidad: \n"))

        if precio < 0:
            print("Error: el precio no puede ser negativo")
            return
        
        if cantidad < 0:
            print("Error: la cantidad no puede ser negativo")
            return

        producto = {
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
        }

        productos.append(producto)

        
        print(f"Producto: '{producto["nombre"]}' se agregó correctamente.")



    except ValueError :
        print("Error: debes ingresar valores válidos")
    finally:
        print("Operacion Terminada.")

























def mostrar_producto():
    print()


def buscar_producto():
    print()

def eliminar_producto():
    print()

def buscar_por_precio():
    print()

def mostrar_estadisticas():
    print()
