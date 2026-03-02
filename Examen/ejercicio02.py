import numpy as np

def f(x):
    return x**3 - 5*x + 1
def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable.")
        return None
    iterations = []
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        iterations.append((a, b, c, f(c)))
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, iterations
def secant_method(f, x0, x1, tol):
    iterations = []
    while True:
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("Error: División por cero en el método de la secante.")
            return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        iterations.append((x0, x1, x2, f(x2)))
        if abs(f(x2)) < tol:
            return x2, iterations
        x0, x1 = x1, x2
a, b = 0, 1
tol = 1e-4
root_bisection, bisection_iterations = bisection_method(f, a, b, tol)
root_secant, secant_iterations = secant_method(f, a, b, tol)
print("Raíz encontrada por el método de bisección:", root_bisection)
print("Raíz encontrada por el método de la secante:", root_secant)
print("\nIteraciones del método de bisección:")
for i, (a, b, c, fc) in enumerate(bisection_iterations):
    print(f"Iteración {i+1}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")
print("\nIteraciones del método de la secante:")
for i, (x0, x1, x2, fx2) in enumerate(secant_iterations):
    print(f"Iteración {i+1}: x0={x0:.6f}, x1={x1:.6f}, x2={x2:.6f}, f(x2)={fx2:.6f}")

