def metodo_trapecio(func, a, b, n):
    """
    Metodo del trapecio para la integracion numerica.

    Parametros:
    func: La funcion a integrar.
    a: El extremo izquierdo del intervalo.
    b: El extremo derecho del intervalo.
    n: El numero de subintervalos.

    Retorna:
    La aproximacion de la integral.
    """
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        integral += func(a + i * h)

    integral *= h
    return integral

#Testing...
if __name__ == "__main__":
    def example_func(x):
        return x**2

    a = 0
    b = 1
    n = 1000

    result = metodo_trapecio(example_func, a, b, n)
    print(f"La integral aproximada es: {result}")
