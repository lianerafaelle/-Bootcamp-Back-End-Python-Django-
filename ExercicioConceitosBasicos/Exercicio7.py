Exercicio7.py

'''Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índice de Massa Corporal(IMC)usandoa fórmula: IMC = peso / (altura x altura)
'''
print("""
====== Calculo de IMC - Índice de Massa Corporal =======     
            Menor que 18,5 -Magreza
            Entre 18,5 e 24,9 -Normal
            Entre 25,0 e 29,9 -Sobrepeso
            Entre 30,0 e 39,9 -Obesidade
            Maior que 40,0 -Obesidade Grave
=========================================================
  """)
try:
    altura = float(input('Qual é a sua Altura em cm: '))
    peso = float(input('Qual é o seu peso em kg: '))
except ValueError:
    print("Por favor, insira números válidos para altura e peso.")
else:
    IMC = peso / ((altura/100) ** 2)
    IMC_arredondado = round(IMC, 1)
    print(f'O valor do seu IMC é {IMC_arredondado}')