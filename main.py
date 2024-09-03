from CalculoRaizC_V1_1 import CalculadorRaiz

if __name__ == '__main__':
    # Obtener los datos del usuario
    valor = float(input('Ingrese el valor de x:\n'))
    iteraciones = int(input('Ingrese el número de interacciones:\n'))

    # Crear un objeto de la clase CalculadorRaiz
    calculador = CalculadorRaiz(valor, iteraciones)

    # Calcular y mostrar la raíz
    raiz = calculador.calcular_raiz()
    print("La raíz aproximada es: {:.2f}".format(raiz))
