def soma (num1,num2): #definição da função soma
        
    calculo = num1+num2
    print(f'o  resultado da soma é : {calculo}')

def subtracao (num1,num2): #definição da função subtração
     sub = num1-num2
     print(f'o resultado da subtração é: {sub}') 
  

def multiplicacao (num1,num2):#definição da função multiplicação
     mult = num1*num2
     print(f'o resultado da multiplicacao é: {mult}')   

#leitura de valores  do usuario fora das funçoes 
num1 = int(input('digite o primeiro numero'))
num2 = int(input('digite o segundo numero'))

soma(num1,num2)  #chamada da função  
subtracao(num1,num2) #chamada da função
multiplicacao(num1,num2) #chamada de função dentro de uma função
