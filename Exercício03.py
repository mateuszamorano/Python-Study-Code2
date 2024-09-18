opcao = 1
while (opcao == 1):
    num = float(input("Digite um número: "))
    if num % 2:
        print(f"O numero digitado é impar: {num}")
    else:
        print(f"O número é par: {num}")
    if num < 0:
        print(f"Este número é negativo. {num}")
    else:
        print(f"Este número é positivo. {num}")
    opcao = int(input("Se quiser continuar, digite 1 para sim e 2 para não: "))