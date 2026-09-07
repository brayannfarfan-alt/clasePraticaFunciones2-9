import pytest
import productos


# decoradores
@pytest.fixture(autouse=True)
def limpiar_productos():
    productos.productos.clear()
    yield # => se ejecuta los test de prueba
    productos.productos.clear()


@pytest.fixture
def datos_base():
    productos.productos.extend([
        {"nombre":"Mouse","precio":1000,"cantidad":3},
        {"nombre":"Teclado","precio":5000,"cantidad":2},
        {"nombre":"Parlante","precio":3000,"cantidad":5}
    ])

    return productos.productos



# def test_agregar_producto_exito( monkeypatch ):

#     entrada = iter(["Mouse","1500","3"]) # usuario, tester

#     monkeypatch.setattr("builtins.input",lambda _: next(entrada))

#     productos.agregar_producto()

#     assert len(productos.productos) > 0


def test_buscar_productos_existentes( datos_base ):

    resultado = productos.buscar_por_precio( datos_base, precio_maximo=4000)

    assert len(resultado) == 2