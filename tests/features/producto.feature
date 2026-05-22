Feature: Cálculo de precios en librería
  Como administrador de la librería
  Quiero calcular precios finales
  Para cobrar correctamente los productos

  Background:
    Given un producto registrado

  @smoke
  Scenario Outline: Aplicar descuentos válidos
    When se aplica un descuento de <descuento>
    Then el descuento aplicado debe ser válido

    Examples:
      | descuento |
      | 0 |
      | 10 |
      | 40 |

  @critical
  Scenario: Rechazar descuento inválido
    When se aplica un descuento de 50
    Then el sistema debe mostrar un error

  @smoke
  Scenario: Calcular precio final
    Given que el producto tiene descuento del 10%
    When el sistema calcula el precio final
    Then el precio final debe ser 107.1

  @regression
  Scenario: Precio final nunca negativo
    When el sistema calcula el precio final
    Then el precio final debe ser mayor o igual a cero

  @critical
  Scenario: Crear producto con precio inválido
    When se intenta crear un producto con precio 0
    Then el sistema debe rechazar el producto