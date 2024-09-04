x = 1.0
a = float(input('Ingrese el valor de x:\n'))
b = int(input('Ingrese el número de interacciones:\n'))

for k in range(0, b):
    x = (x + a / x) / 2
    print("La raiz despues de ", k, "interaciones es: {:.2f}".format(x))
