import numpy as np

dados_alunos = np.array([[8.0, 7.5, 9.0], [6.0, 5.5, 6.5], [10.0, 9.0, 9.5]])

medias = np.mean(dados_alunos, axis=1)

for i, media in enumerate(medias):
    print(f"Média do Aluno {i+1}: {media:.2f}")
