Exercicio3.py

while True:
    try:
        nota = float(input("Digite uma nota entre zero e dez: "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break  # Sai do loop se a nota for válida
        else:
            print("Nota inválida. Digite um valor entre zero e dez.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")
