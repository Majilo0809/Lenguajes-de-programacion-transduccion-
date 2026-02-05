class Recomendador:
    def __init__(self):
        self.compras = {}

    def addPurchase(self, usuario, producto):
        if usuario not in self.compras:
            self.compras[usuario] = []

        if producto not in self.compras[usuario]:
            self.compras[usuario].append(producto)

    def getRecommendations(self, usuario):
        if usuario not in self.compras:
            return []

        productos_usuario = self.compras[usuario]
        recomendaciones = []

        for otro_usuario in self.compras:
            if otro_usuario != usuario:
                for producto in self.compras[otro_usuario]:
                    if producto not in productos_usuario and producto not in recomendaciones:
                        recomendaciones.append(producto)

        return recomendaciones


# Salida ej

sistema = Recomendador()

# Compras de ejemplo
sistema.addPurchase("Ana", "Laptop")
sistema.addPurchase("Ana", "Teclado")

sistema.addPurchase("Luis", "Laptop")
sistema.addPurchase("Luis", "Mouse")

sistema.addPurchase("Maria", "Laptop")
sistema.addPurchase("Maria", "Audifonos")

usuario = input("Ingrese el nombre del usuario: ")
recs = sistema.getRecommendations(usuario)

if recs:
    print("Productos recomendados:")
    for r in recs:
        print("-", r)
else:
    print("No hay recomendaciones disponibles")
