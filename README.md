# Lenguajes-programacion-transduccion-

# Problema 1
Se implementó un sistema que simula el funcionamiento básico de un navegador web utilizando una clase llamada Navegador. El sistema mantiene la página actual y dos listas que representan el historial de navegación: una para retroceder y otra para avanzar.

Funcionamiento:
- Cuando el usuario carga una nueva página, la página actual se guarda en la lista de páginas anteriores.
- Al retroceder, la página actual pasa a la lista de páginas siguientes y se recupera la última página visitada, y al avanzar ocurre el proceso inverso.
- Opción de recargar la página actual.
El sistema se controla mediante un menú interactivo en consola.
+ Se usan: clases, pilas, métodos, condicionales y ciclos.


# Problema 2
Se desarrolló un sistema de autocompletado utilizando una clase llamada Autocomplete, que almacena palabras en una lista y permite buscar coincidencias a partir de un prefijo ingresado por el usuario.

Funcionamiento:
- Las palabras se agregan al sistema mediante el método insert.
- Cuando el usuario ingresa un prefijo, el método autocomplete recorre la lista de palabras.
- Se comparan las palabras almacenadas con el prefijo y se guardan aquellas que coinciden.
- Se devuelve una lista con todas las coincidencias encontradas.
+ Se usan: listas, recorridos con ciclos, condicionales y cadenas de texto.


# Problema 3
Se implementó un sistema de recomendación basado en las relaciones entre usuarios y productos mediante una clase llamada Recomendador. El sistema analiza las compras realizadas por distintos usuarios para sugerir productos.

Funcionamiento:
- Las compras se almacenan en un diccionario que relaciona cada usuario con los productos adquiridos.
- El método addPurchase registra nuevas compras.
- El método getRecommendations compara las compras del usuario con las de otros usuarios.
- Se recomiendan productos que el usuario aún no ha comprado, pero que otros usuarios sí.
+ Se usan: diccionarios, listas, ciclos anidados, condicionales y encapsulación mediante clases.
