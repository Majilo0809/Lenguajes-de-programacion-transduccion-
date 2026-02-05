class Autocomplete:
    def __init__(self):
        self.palabras = []

    def insert(self, word):
        self.palabras.append(word)

    def autocomplete(self, prefix):
        resultados = []

        for palabra in self.palabras:
            # SW verifica q la palabra comience con el prefijo
            if palabra.startswith(prefix):
                resultados.append(palabra)

        return resultados

auto = Autocomplete()

# Palabras bases
auto.insert("cascara")
auto.insert("carrito")
auto.insert("camaleon  ")
auto.insert("computadora")
auto.insert("perro")
auto.insert("piso")
auto.insert("pelota")

while True:
    print("\n- - AUTOCOMPLETAR - -")
    print("1| Agregar palabra")
    print("2| Buscar por prefijo")
    print("3| Salir")

    eleccion = input("Seleccione una opcion: ")

    if eleccion == "1":
        palabra = input("Ingrese la palabra: ")
        auto.insert(palabra)
        print("Palabra agregada")

    elif eleccion == "2":
        prefijo = input("Ingrese el prefijo: ")
        resultados = auto.autocomplete(prefijo)
        if resultados:
            print("Coincidencias encontradas:")
            for r in resultados:
                print("-", r)
        else:
            print("No se encontraron coincidencias")

    elif eleccion == "3":
        print("Saliendo...")
        break

    else:
        print("Opcion no valida")
