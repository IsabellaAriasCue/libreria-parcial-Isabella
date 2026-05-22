**SM-1 (0.3 puntos)**

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

- **Respuesta: C**
- Justificación: Es el tradicciónal ya que los demás mencionados no tienen el enfoque del que habla el enunciado como tal.

**SM-2 (0.3 puntos)**

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

- **Respuesta: B**
- Justificación: Porque se está saltando el ciclo RED, que es el de solo hacer las pruebas sin haber desarrollado la implementación lo cual ocasionará que falle. 


## **PREGUNTAS ABIERTAS**
*Responde con tus propias palabras. La extensión ideal es entre 5 y 8 líneas por pregunta. No se piden definiciones de diccionario: se pide que demuestres que entendiste el concepto.*

**PA-1 (0.3 puntos)**

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

- Porque sí no lo hiciera no estaria cumpliendo con el RED-GREEN-REFACTOR que es lo que se supone que busca implementar en su desarrollo, 
segundo el saltarse el proceso puede verse reflejado en los tiempos de entrega al hacerlo "limpio y completo".
---

**PA-2 (0.3 puntos)**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.

- **TDD:** Es un enfoque que se toma para desarrollar en donde se dice que hay 3 fases RED - GREEN - REFACTOR y en cada una suceden cosas diferentes, este esta mas
orientado a la manera es que se desarrollan funcionalidades.
- **BDD:** Se usa buscando que personas no técnicas puedan comprender el "flujo de todo lo que pasa" utilizando un lenguage más humano utilizando Given, When, Then se describen scenarios y ya luego de tener esto usando el **Gherkin** tambien se pueden realizar las pruebas basadas en el contenido que este tiene.
---

**PA-3 (0.3 puntos)**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.

- Tener una alta cobertura de código es excelente, pero no garantiza que un sistema esté libre de bugs. La cobertura mide qué líneas de código se ejecutaron durante las pruebas, pero no evalúa si la lógica es correcta, o si quizas faltan casos extremos o si el programa esta o no manejando bien los datos que resultan inesperados.

Ejemplo sencillo:

def es_par(numero): return numero % 2 == 1

Las pruebas llaman la función y alcanzan una cobertura muy alta, pero la lógica está mal, porque devuelve True para números impares y no para pares.

Por ejemplo: es_par(8) debería dar True pero devuelve False
Entonces, aunque el código sí fue probado, el programa todavía tiene un bug.



---

**PA-4 (0.2 puntos)**

En el contexto de la Regla 2 del examen (descuento entre 0% y 40%), un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

- Probar solo 20% 0% no valida los bordes del rango. Los errores también pueden aparecer en límites. Yo probaría:

-1% → inválido
0% → válido
1% → válido
39% → válido
40% → válido
41% → inválido

Porque los límites son donde normalmente fallan las validaciones.

---

**PA-5 (0.3 puntos)**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 6. ¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?

- CI/CD depende de pruebas automáticas para validar cambios rápidamente. TDD y BDD ayudan a construir lo que permite que que el pipeline puede ejecutar automáticamente. Sin tests automatizados el pipeline no detecta errores y podrían desplegarse fallos a producción.