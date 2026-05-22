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