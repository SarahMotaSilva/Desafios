from src.calculos import calcular_estagiario, calcular_clt, calcular_freelancer


def cadastrar_funcionario():
    """Valida entradas e retorna um dicionário[cite: 84, 95]."""
    try:
        nome = input("Nome: ").strip()
        if not nome:
            raise ValueError("Nome obrigatório[cite: 35].")

        tipo = input("Tipo (estagiario, clt, freelancer): ").strip().lower()
        if tipo not in ["estagiario", "clt", "freelancer"]:
            raise ValueError("Tipo inválido[cite: 36].")

        if tipo == "freelancer":
            v_hora = float(input("Valor/hora: "))
            horas = float(input("Horas trabalhadas: "))
            if v_hora <= 0 or horas <= 0:
                raise ValueError("Devem ser > 0[cite: 38].")
            res = calcular_freelancer(v_hora, horas)
        else:
            base = float(input("Salário base: "))
            if base <= 0:
                raise ValueError("Deve ser > 0[cite: 37].")
            res = (
                calcular_estagiario(base)
                if tipo == "estagiario"
                else calcular_clt(base)
            )

        return {
            "nome": nome,
            "tipo": tipo.capitalize(),
            "bruto": res[0],
            "inss": res[1],
            "irrf": res[2],
            "liquido": res[3],
        }
    except ValueError as e:
        print(f"Erro: {e} [cite: 39]")
        return None
