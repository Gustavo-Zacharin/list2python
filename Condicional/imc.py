nome = str(input('Digite seu nome: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2

print(f'{nome}, seu IMC com base em seu peso e altura é {imc:.1f}')

if imc < 18.5:
    print(f'Seu IMC está abaixo do peso!')
elif 18.5 <= imc <= 24.9: 
    print(f'Seu IMC está saudável!')
elif 25.0 <= imc <= 29.9:
    print(f'Seu IMC está acima do peso!')
else: 
    print(f"Seu imc consta obesidade")


    