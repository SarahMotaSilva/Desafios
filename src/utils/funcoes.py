import random


def criar_matriz_aleatoria(linhas, colunas):
    return [[random.randint(1, 10) for _ in range(colunas)] for _ in range(linhas)]


def exibir_matriz(titulo, matriz):
    print(f"\n--- {titulo} ---")
    for linha in matriz:
        print(linha)
