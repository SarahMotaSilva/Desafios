import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.funcoes import criar_matriz_aleatoria, exibir_matriz


def resolver_exercicios():
    matriz_3x3 = criar_matriz_aleatoria(3, 3)
    exibir_matriz("Matriz 3x3 Aleatória", matriz_3x3)

    notas = np.array(matriz_3x3)
    medias = np.mean(notas, axis=1)
    print("\nMédias por linha (NumPy):", medias)

    if matriz_3x3:
        det = np.linalg.det(notas)
        print(f"\nDeterminante da matriz: {det:.2f}")


if __name__ == "__main__":
    resolver_exercicios()
