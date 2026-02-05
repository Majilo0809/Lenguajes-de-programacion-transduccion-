class Navegador:
    def __init__(self):
        self.atras = []
        self.adelante = []
        self.actual = "Google"

    def mostrar_pagina(self):
        print("\nPagina actual:", self.actual)

    def loadPage(self, url):
        self.atras.append(self.actual)
        self.actual = url
        self.adelante.clear()
        self.mostrar_pagina()

    def goBack(self):
        if not self.atras:
            print("No hay paginas anteriores")
            return
        self.adelante.append(self.actual)
        self.actual = self.atras.pop()
        self.mostrar_pagina()

    def goForward(self):
        if not self.adelante:
            print("No hay paginas siguientes")
            return
        self.atras.append(self.actual)
        self.actual = self.adelante.pop()
        self.mostrar_pagina()

    def recargar(self):
        print("Refrescando pagina...")
        self.mostrar_pagina()


# Simulacion de pagina

navegador = Navegador()

paginas = {
    "1": "Google",
    "2": "YouTube",
    "3": "Gmail"
}

while True:

    print("\n--- Menu Navegador ---")
    print("1| Ir a Google")
    print("2| Ir a YouTube")
    print("3| Ir a Gmail")
    print("4| Atras")
    print("5| Adelante")
    print("6| Refrescar pagina")
    print("7| Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion in paginas:
        navegador.loadPage(paginas[opcion])
    elif opcion == "4":
        navegador.goBack()
    elif opcion == "5":
        navegador.goForward()
    elif opcion == "6":
        navegador.recargar()
    elif opcion == "7":
        print("Cerrando...")
        break
    else:
        print("Opción no disponible")
