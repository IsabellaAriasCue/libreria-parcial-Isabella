# Particiones de Equivalencia

### Regla 1 — Precio base mayor que cero

| Partición                | Rango | Valor representativo | Resultado esperado |
| ------------------------ | ----- | -------------------- | ------------------ |
| Precio válido            | > 0   | 100                  | Producto creado    |
| Precio inválido negativo | < 0   | -50                  | Error              |
| Precio inválido cero     | = 0   | 0                    | Error              |

---

### Regla 2 — Descuento entre 0% y 40%

| Partición                   | Rango    | Valor representativo | Resultado esperado |
| --------------------------- | -------- | -------------------- | ------------------ |
| Descuento válido            | 0% - 40% | 20%                  | Descuento aplicado |
| Descuento inválido negativo | < 0%     | -5%                  | Error              |
| Descuento inválido alto     | > 40%    | 50%                  | Error              |

---

## Valores Límite — Regla 2

| Valor | Dentro/Fuera | Resultado esperado |
| ----- | ------------ | ------------------ |
| -1%   | Fuera        | Error              |
| 0%    | Dentro       | Válido             |
| 1%    | Dentro       | Válido             |
| 39%   | Dentro       | Válido             |
| 40%   | Dentro       | Válido             |
| 41%   | Fuera        | Error              |

---

## Pregunta al Administrador

## Pregunta

¿El sistema debe redondear el precio final a dos decimales después de aplicar descuento e IVA?¿o prefiere que sea de otro modo?

##### Justificación

Esta pregunta impacta el diseño de los casos de prueba porque el resultado esperado puede cambiar dependiendo de cómo el sistema maneje los decimales.


--- 
## PARTE 2 — Casos de Prueba

| ID    | Regla | Descripción                         | Precondición    | Datos de entrada              | Pasos                 | Resultado esperado | Tipo     |
| ----- | ----- | ----------------------------------- | --------------- | ----------------------------- | --------------------- | ------------------ | -------- |
| CP-01 | R1    | Crear producto con precio válido    | Ninguna         | Precio = 100                  | Crear producto        | Producto creado    | Positivo |
| CP-02 | R1    | Crear producto con precio negativo  | Ninguna         | Precio = -50                  | Crear producto        | Error              | Negativo |
| CP-03 | R1    | Crear producto con precio cero      | Ninguna         | Precio = 0                    | Crear producto        | Error              | Borde    |
| CP-04 | R2    | Aplicar descuento válido            | Producto creado | 20%                           | Aplicar descuento     | Descuento aplicado | Positivo |
| CP-05 | R2    | Aplicar descuento mayor a 40%       | Producto creado | 50%                           | Aplicar descuento     | Error              | Negativo |
| CP-06 | R2    | Aplicar descuento de 40%            | Producto creado | 40%                           | Aplicar descuento     | Descuento aplicado | Borde    |
| CP-07 | R3    | Calcular precio final correctamente | Producto creado | Precio = 100, descuento = 10% | Calcular precio final | Resultado correcto | Positivo |
| CP-08 | R3    | Precio final nunca negativo         | Producto creado | Precio = 100                  | Calcular precio final | Precio >= 0        | Positivo |
