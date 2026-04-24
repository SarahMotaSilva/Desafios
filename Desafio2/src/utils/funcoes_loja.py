from src.utils.validacoes import input_string, input_float, input_int


def cadastrar_produto(produtos):
    nome = input_string("Nome do produto: ")

    if any(p["nome"].lower() == nome.lower() for p in produtos):
        print("Produto já existe.")
        return

    preco = input_float("Preço: ")
    estoque = input_int("Estoque: ")

    produtos.append({"nome": nome, "preco": preco, "estoque": estoque})

    print("Produto cadastrado com sucesso!")


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for i, produto in enumerate(produtos):
        print(
            f"{i + 1}. {produto['nome']} - "
            f"R$ {produto['preco']:.2f} - "
            f"Estoque: {produto['estoque']}"
        )


def calcular_venda(produto, quantidade):
    valor_bruto = produto["preco"] * quantidade

    desconto = 0
    if quantidade > 10:
        desconto = valor_bruto * 0.05

    valor_final = valor_bruto - desconto

    produto["estoque"] -= quantidade

    return {
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final,
    }


def realizar_venda(produtos, vendas):
    if not produtos:
        print("Sem produtos disponíveis.")
        return

    cliente = input_string("Nome do cliente: ")

    listar_produtos(produtos)

    try:
        indice = int(input("Escolha o produto (número): ")) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    if indice < 0 or indice >= len(produtos):
        print("Produto inválido.")
        return

    produto = produtos[indice]

    quantidade = input_int("Quantidade: ")

    if quantidade == 0:
        print("Quantidade deve ser maior que zero.")
        return

    if quantidade > produto["estoque"]:
        print("Estoque insuficiente.")
        return

    venda = calcular_venda(produto, quantidade)
    venda["cliente"] = cliente

    vendas.append(venda)

    print("Venda realizada com sucesso!")


def gerar_relatorio(vendas):
    if not vendas:
        print("Nenhuma venda realizada.")
        return

    total = 0

    print("\n=== Relatório de Vendas ===\n")

    for venda in vendas:
        print(f"Cliente: {venda['cliente']}")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Valor Bruto: R$ {venda['valor_bruto']:.2f}")
        print(f"Desconto: R$ {venda['desconto']:.2f}")
        print(f"Valor Final: R$ {venda['valor_final']:.2f}")
        print()

        total += venda["valor_final"]

    print(f"Total arrecadado: R$ {total:.2f}")


def salvar_relatorio(vendas):
    try:
        with open("relatorio_vendas.txt", "w", encoding="utf-8") as arquivo:
            total = 0

            for venda in vendas:
                arquivo.write(f"Cliente: {venda['cliente']}\n")
                arquivo.write(f"Produto: {venda['produto']}\n")
                arquivo.write(f"Quantidade: {venda['quantidade']}\n")
                arquivo.write(f"Valor Bruto: R$ {venda['valor_bruto']:.2f}\n")
                arquivo.write(f"Desconto: R$ {venda['desconto']:.2f}\n")
                arquivo.write("Valor Final: R$ " f"{venda['valor_final']:.2f}\n\n")

                total += venda["valor_final"]

            arquivo.write(f"Total arrecadado: R$ {total:.2f}\n")

        print("Relatório salvo com sucesso!")

    except OSError as erro:
        print(f"Erro ao salvar arquivo: {erro}")
