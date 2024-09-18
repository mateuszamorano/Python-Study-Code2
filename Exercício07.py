sal = 1293.20
salus = float(input("Digite seu salário: "))
divid = salus / sal
print(f"O seu salário é: {divid:.2f} maior que o mínimo")
if salus < sal:
    print("Acione a Justiça do Trabalho.")