import pytest

from app.producto import Producto


def test_crear_producto_con_precio_valido():
    producto = Producto("Libro", 100)

    assert producto.precio_base == 100


def test_no_permitir_precio_negativo():

    with pytest.raises(ValueError):
        Producto("Libro", -50)


def test_no_permitir_precio_cero():

    with pytest.raises(ValueError):
        Producto("Libro", 0)

#R2
def test_aplicar_descuento_valido():

    producto = Producto("Libro", 100)

    producto.aplicar_descuento(20)

    assert producto.descuento == 20


def test_no_permitir_descuento_mayor_a_40():

    producto = Producto("Libro", 100)

    with pytest.raises(ValueError):
        producto.aplicar_descuento(50)


def test_permitir_descuento_cero():

    producto = Producto("Libro", 100)

    producto.aplicar_descuento(0)

    assert producto.descuento == 0

def test_calcular_precio_final():

    producto = Producto("Libro", 100)

    producto.aplicar_descuento(10)

    assert producto.calcular_precio_final() == 107.1


def test_precio_final_no_negativo():

    producto = Producto("Libro", 100)

    resultado = producto.calcular_precio_final()

    assert resultado >= 0