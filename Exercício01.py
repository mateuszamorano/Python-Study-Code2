vala = float(input("Digite o primeiro valor: "))
valb = float(input("Digite o segundo valor: "))
valc = float(input("Digite o terceiro valor: "))
resul = vala + valb
if resul < valc:
    print(f"A soma do valor A com o B foi menor que C, então o resultado é: {valc}")
else:
    print(f"A soma dos Valores A e B foram maior que C, então o resultado é: {resul}")