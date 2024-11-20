def newton_raphson_method(func, deriv, x0, tol, max_iter):
    """
    Metodo de Newton-Raphson para encontrar la raiz de una funcion.

    Parametros:
    func: La funcion la cual se debe encontrar la raiz.
    deriv: La derivada de la funcion.
    x0: El valor inicial.
    tol: Margen de error permitido.
    max_iter: El numero maximo de iteraciones permitidas.

    Retorna:
    Una tupla que contiene la raiz aproximada y el numero de iteraciones realizadas.
    """
    x = x0
    iter_count = 0

    for _ in range(max_iter):
        iter_count += 1
        fx = func(x)
        dfx = deriv(x)
        
        if dfx == 0:
            print("La derivada es cero. No se puede continuar.")
            return None, iter_count
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            return x_new, iter_count
        
        x = x_new
    
    print("Se alcanzo el numero maximo de iteraciones.")
    return x, iter_count

# testing...
def func(x):
    return x**3 - 4*x**2 - 7

def deriv(x):
    return 3*x**2 - 8*x

x0 = 5
tol = 0.0001
max_iter = 100

root, iterations = newton_raphson_method(func, deriv, x0, tol, max_iter)
print(f"La raiz aproximada es: {root}")
print(f"Numero de iteraciones: {iterations}")
