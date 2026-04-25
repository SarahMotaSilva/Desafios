def cadastrar():
    nome = input("Nome: ").strip()
    tipo = input("Tipo (estagiario/clt/freelancer): ").lower()

    if tipo == "estagiario":
        salario = float(input("Salário: "))
        return {"nome": nome, "tipo": tipo, "salario": salario}

    elif tipo == "clt":
        salario = float(input("Salário: "))
        return {"nome": nome, "tipo": tipo, "salario": salario}

    elif tipo == "freelancer":
        horas = float(input("Horas: "))
        valor = float(input("Valor/hora: "))
        return {"nome": nome, "tipo": tipo, "horas": horas, "valor": valor}

    else:
        print("Tipo inválido")
        return None
