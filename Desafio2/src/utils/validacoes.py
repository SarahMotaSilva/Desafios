def input_string(msg):
    while True:
        valor = input(msg).strip()
        if valor:
            return valor
        print("Entrada inválida. Tente novamente.")


def input_float(msg):
    while True:
        try:
            valor = float(input(msg))
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")


def input_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor >= 0:
                return valor
            print("O valor deve ser maior ou igual a zero.")
        except ValueError:
            print("Digite um número inteiro válido.")
