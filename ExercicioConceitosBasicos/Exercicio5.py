Exercicio5.py

def calcular_salario_liquido(salario_bruto):
    # Definindo as faixas de imposto de renda
    faixas = [(1903.99, 2826.65, 0.075), (2826.66, 3751.05, 0.15), (3751.06, 4664.68, 0.225), (4664.68, float('inf'), 0.275)]

    # Calculando o imposto de renda
    imposto_renda = 0
    for faixa in faixas:
        if salario_bruto > faixa[0]:
            imposto_renda += (min(salario_bruto, faixa[1]) - faixa[0]) * faixa[2]

    # Calculando o salário líquido
    salario_liquido = salario_bruto - imposto_renda

    return salario_liquido

# Exemplo de uso
salario_bruto = float(input("Informe o salário bruto: R$ "))
salario_liquido = calcular_salario_liquido(salario_bruto)

print(f"Salário Líquido: R$ {salario_liquido:.2f}")
