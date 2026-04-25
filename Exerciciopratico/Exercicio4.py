import numpy as np

coeficientes = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

det = np.linalg.det(coeficientes)
print(f"Determinante: {det:.2f}")

if det != 0:
    print("O sistema é resolvível (possui solução única).")
else:
    print("O sistema não é resolvível ou possui infinitas soluções.")
