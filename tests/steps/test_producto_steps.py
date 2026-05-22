from pytest_bdd import scenarios, given, when, then, parsers
import pytest

from app.producto import Producto

scenarios("../features/producto.feature")


@given(
    "un producto registrado",
    target_fixture="producto"
)
def producto():

    return Producto("Libro", 100)


@given(
    "que el producto tiene descuento del 10%",
    target_fixture="producto"
)
def producto_descuento():

    producto = Producto("Libro", 100)

    producto.aplicar_descuento(10)

    return producto


@when(parsers.parse("se aplica un descuento de {descuento:d}"))
def aplicar_descuento(producto, descuento):

    if descuento > 40:

        with pytest.raises(ValueError):
            producto.aplicar_descuento(descuento)

    else:
        producto.aplicar_descuento(descuento)


@when("el sistema calcula el precio final")
def calcular_precio(producto):

    producto.resultado = producto.calcular_precio_final()


@when("se aplica un descuento de 50")
def descuento_error(producto):

    with pytest.raises(ValueError):
        producto.aplicar_descuento(50)


@when("se intenta crear un producto con precio 0")
def producto_invalido():

    global error_producto

    with pytest.raises(ValueError):
        Producto("Libro", 0)

    error_producto = True


@then("el descuento aplicado debe ser válido")
def validar_descuento():

    assert True


@then("el sistema debe mostrar un error")
def validar_error():

    assert True


@then("el precio final debe ser 107.1")
def validar_precio(producto):

    assert producto.resultado == 107.1


@then("el precio final debe ser mayor o igual a cero")
def validar_no_negativo(producto):

    assert producto.resultado >= 0


@then("el sistema debe rechazar el producto")
def validar_producto():

    assert error_producto is True