from productos import (
    agregar_producto,
    #mostrar_productos,
    # buscar_por_precio,
    # buscar_producto,
    # eliminar_producto,
    # mostrar_estadisticas,
    # mostrar_producto
)
from menu import mostrar_menu



# import productos




def index():
    while True:
        mostrar_menu()

        op = input("Selecionar : ").strip()

        match op :
            case "1": 
                agregar_producto()






if __name__ == "__main__":
    index()