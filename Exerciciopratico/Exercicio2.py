vendas_semana1 = [[100, 200], [150, 300]]
vendas_semana2 = [[120, 180], [130, 250]]

total_vendas = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        total_vendas[i][j] = vendas_semana1[i][j] + vendas_semana2[i][j]

print("Total de Vendas (Semana 1 + Semana 2):", total_vendas)
