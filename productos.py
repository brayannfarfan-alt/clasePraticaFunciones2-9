

productos = []


def agregar_producto():

    print("\n===== AGREGAR PRODUCTO =====")

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



def mostrar_productos():
    print("\n===== LISTA DE PRODUCTOS =====")

    if not productos:
        print("No hay productos registrados.")
        return

    for indice, producto in enumerate(productos, start=1):
        print(f"""
        Producto #{indice}
        Nombre:   {producto["nombre"]}
        Precio:   ${producto["precio"]:.2f}
        Cantidad: {producto["cantidad"]}
        ------------------------------
    """)


def buscar_producto():
    print("\n===== BUSCAR PRODUCTO =====")

    if not productos:
        print("No hay productos registrados.")
        return

    nombre_buscado = input("Ingrese el nombre del producto: ").strip()

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print("\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            return

    print("Producto no encontrado.")



def eliminar_producto():
    print("\n===== ELIMINAR PRODUCTO =====")

    if not productos:
        print("No hay productos registrados.")
        return

    nombre_buscado = input("Ingrese el nombre del producto: ").strip()

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            productos.remove(producto)

            print(
                f"Producto '{producto['nombre']}' "
                "eliminado correctamente."
            )
            return

    print("Producto no encontrado.")


def buscar_por_precio():
    print("\n===== BUSCAR POR PRECIO =====")

    if not productos:
        print("No hay productos registrados.")
        return

    try:
        precio_maximo = float(
            input("Mostrar productos hasta un precio de: ")
        )

        if precio_maximo < 0:
            print("El precio no puede ser negativo.")
            return

        encontrados = []

        for producto in productos:
            if producto["precio"] <= precio_maximo:
                encontrados.append(producto)

        if not encontrados:
            print("No se encontraron productos.")
            return

        print("\nProductos encontrados:")

        for producto in encontrados:
            print(
                f"- {producto['nombre']} "
                f"| ${producto['precio']:.2f}"
            )

    except ValueError:
        print("Error: debes ingresar un precio válido.")


def mostrar_estadisticas():
    print("\n===== ESTADÍSTICAS =====")

    if not productos:
        print("No hay productos registrados.")
        return

    cantidad_productos = len(productos)

    valor_total = 0

    for producto in productos:
        valor_total += (
            producto["precio"] *
            producto["cantidad"]
        )

    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
