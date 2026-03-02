import numpy as np

A = np.array([[1, 1, 1],
                [2, -1, 3],
                [-1, 2, 2]], dtype=float)
b = np.array([6, 9, 9], dtype=float)

det_A = np.linalg.det(A)
if det_A == 0:
    print("El sistema no tiene solución única.")
else:
    print("El sistema tiene solución única.")
    # Método de Gauss-Jordan con pivoteo
    n = len(b)
    
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        # Pivoteo: buscar el máximo en la columna i
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        if max_row != i:
            Ab[[i, max_row]] = Ab[[max_row, i]]
        # Normalizar la fila pivote
        Ab[i] = Ab[i] / Ab[i][i]
        for j in range(n):
            if i != j:
                Ab[j] = Ab[j] - Ab[i] * Ab[j][i]

    solution = Ab[:, -1]
    print("La solución es:")
    print(f"x = {solution[0]:.2f}, y = {solution[1]:.2f}, z = {solution[2]:.2f}")

