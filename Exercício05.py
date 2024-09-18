opcao = 1
while opcao == 1:
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))
    if val1 == val2:
        c = val1 + val2
        print(f"Como os valores foram iguais, a soma deles é: {c}")
    else:
        c = val1 * val2
        print(f"Como os valores não foram iguais, houve a multiplicação dos mesmos: {c}")
    opcao = int(input(f"Digite 1 para continuar o processo e 2 para finalizar: "))
if opcao == 2:
    print("O sistema foi encerrado!")