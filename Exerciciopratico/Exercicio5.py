import numpy as np

estoque = np.array([[10, 20, 30], [5, 15, 25]])

precos = np.array([[10.0], [12.0], [11.0]])

estoque_T = estoque.T

totais_por_produto = np.dot(estoque, precos)

print("Valor total em estoque por produto:\n", totais_por_produto)
