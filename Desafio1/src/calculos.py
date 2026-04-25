def calcular_estagiario(salario_fixo):
    """Regra: Salário fixo sem descontos[cite: 22, 23]."""
    return salario_fixo, 0.0, 0.0, salario_fixo


def calcular_clt(salario_bruto):
    """Regra: 8% INSS e 10% IRRF se > R$ 2000[cite: 27, 28]."""
    inss = salario_bruto * 0.08
    irrf = (salario_bruto * 0.10) if salario_bruto > 2000 else 0.0
    liquido = salario_bruto - inss - irrf
    return salario_bruto, inss, irrf, liquido


def calcular_freelancer(valor_hora, horas):
    """Regra: Valor/hora x Horas com 5% de desconto fixo[cite: 31, 32]."""
    bruto = valor_hora * horas
    desconto = bruto * 0.05
    liquido = bruto - desconto
    return bruto, desconto, 0.0, liquido
