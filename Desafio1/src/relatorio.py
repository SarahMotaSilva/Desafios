import os


def gerar_texto_relatorio(funcionarios):
    """Formata o relatório conforme o exemplo[cite: 41, 50]."""
    texto = "=== Relatório de Folha de Pagamento ===\n"
    total = 0
    for f in funcionarios:
        texto += (
            f"Nome: {f['nome']}\nTipo: {f['tipo']}\n"
            f"Salário Bruto: R$ {f['bruto']:.2f}\n"
            f"Desconto INSS: R$ {f['inss']:.2f}\n"
            f"Desconto IRRF: R$ {f['irrf']:.2f}\n"
            f"Salário Líquido: R$ {f['liquido']:.2f}\n" + "-" * 30 + "\n"
        )
        total += f["liquido"]
    texto += f"Total pago pela empresa: R$ {total:.2f}\n"
    return texto


def salvar_em_arquivo(conteudo):
    """Salva o relatório em TXT com tratamento de erros[cite: 74, 76]."""
    try:
        caminho = "relatorio_folha.txt"
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"Salvo em: {os.path.abspath(caminho)} [cite: 75]")
    except OSError as e:
        print(f"Erro de permissão ou escrita: {e} [cite: 116]")
