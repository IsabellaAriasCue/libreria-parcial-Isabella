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
