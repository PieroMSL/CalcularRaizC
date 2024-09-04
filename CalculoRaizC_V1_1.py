class CalculadorRaiz:
    def __init__(self, valor, iteraciones):
        self.valor = valor
        self.iteraciones = iteraciones

    def calcular_raiz(self):
        x = 1.0
        for k in range(0, self.iteraciones):
            x = (x + self.valor / x) / 2
            print("La raíz después de", k, "iteraciones es", x)
        return x