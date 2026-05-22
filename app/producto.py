class Producto:

    PRECIO_MINIMO = 0

    def __init__(self, nombre, precio_base):

        if precio_base <= self.PRECIO_MINIMO:
            raise ValueError(
                "El precio debe ser mayor que cero"
            )

        self.nombre = nombre
        self.precio_base = precio_base