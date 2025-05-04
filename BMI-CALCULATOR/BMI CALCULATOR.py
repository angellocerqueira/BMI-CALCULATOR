print('CALCULADORA DE IMC')
print('=' * 30)

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'\n{nome}, seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso normal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 35:
    print('Obesidade grau 1.')
elif imc < 40:
    print('Obesidade grau 2.')
else:
    print('Obesidade grau 3 (mórbida).')
