class Producto:

    PRECIO_MINIMO = 0

    def __init__(self, nombre, precio_base):

        if precio_base <= self.PRECIO_MINIMO:
            raise ValueError(
                "El precio debe ser mayor que cero"
            )

        self.nombre = nombre
        self.precio_base = precio_base

class Producto:

    PRECIO_MINIMO = 0
    DESCUENTO_MAXIMO = 40

    def __init__(self, nombre, precio_base):

        if precio_base <= self.PRECIO_MINIMO:
            raise ValueError(
                "El precio debe ser mayor que cero"
            )

        self.nombre = nombre
        self.precio_base = precio_base
        self.descuento = 0

    def aplicar_descuento(self, descuento):

        if descuento < 0 or descuento > self.DESCUENTO_MAXIMO:
            raise ValueError(
                "El descuento debe estar entre 0 y 40"
            )

        self.descuento = descuento