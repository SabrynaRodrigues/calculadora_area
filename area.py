# Calculadora para área de terreno retangular - Sabryna Rodrigues 11/07/2022
def area(a,b):
    calc = a * b
    print(f'A área do terreno é igual à {calc}m².')


# Programa Principal
print('【 Calcule a área de um terreno retangular 】')
while True:
    a = float(input('Largura do terreno:'))
    b = float(input('Comprimento do terreno:'))
    area(a,b)
    cont = str(input(': ̗̀➛ Deseja continuar? S/N')).upper()
    if cont not in 'S':
        break
