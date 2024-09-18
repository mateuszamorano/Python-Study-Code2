peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f"Seu IMC é de: {imc:.2f} e você está abaixo do peso!")
elif imc >= 18.6 and imc <= 24.9:
    print(f"Seu IMC é de: {imc:.2f} e você está no peso ideal, parabéns!")
elif imc >= 25 and imc <= 29.9:
    print(f"Seu IMC é de: {imc:.2f} e você está levemente acima do peso!")
elif imc >= 30 and imc <= 34.9:
    print(f"Seu IMC é de: {imc:.2f} e você está com obesidade grau 1!")
elif imc >= 35 and imc <=39.9:
    print(f"Seu IMC é de: {imc:.2f} e você está com obesidade grau 2!")
elif imc >= 40:
    print(f"Seu IMC é de: {imc:.2f} e você com obesidade grau 3 (mórbida)!")