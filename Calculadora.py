cores = {'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m',
         'lilás': '\033[1;35m',
         'limpar': '\033[m',}

titulo = 'Calculadora Simples'
linha = '-=-' * 10
print(f'''{cores["vermelho"]}{linha}
{titulo.center(30)}
{linha}{cores["limpar"]}''')

n1 = int(input(f'Digite o {cores["verde"]}1°{cores["limpar"]} número inteiro: '))
n2 = int(input(f'Digite o {cores["azul"]}2°{cores["limpar"]} número inteiro: '))
while True:
    operacao = int(input('''\n[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
Qual a operação desejada? '''))
    print('')
    if operacao == 1:
        print(f'{cores["verde"]}{n1}{cores["limpar"]} + {cores["lilás"]}{n2}{cores["limpar"]} = {cores["azul"]}{n1 + n2}{cores["limpar"]}')
    elif operacao == 2:
        print(f'{cores["verde"]}{n1}{cores["limpar"]} - {cores["lilás"]}{n2}{cores["limpar"]} = {cores["azul"]}{n1 - n2}{cores["limpar"]}')
    elif operacao == 3:
        print(f'{cores["verde"]}{n1}{cores["limpar"]} * {cores["lilás"]}{n2}{cores["limpar"]} = {cores["azul"]}{n1 * n2}{cores["limpar"]}')
    elif operacao == 4:
        print(f'{cores["verde"]}{n1}{cores["limpar"]} / {cores["lilás"]}{n2}{cores["limpar"]} = {cores["azul"]}{n1 / n2}{cores["limpar"]}')
    else:
        print('{cores["vermelho"]}Operação inválida. Tente novamente!{cores["limpar"]}')
        continue
    continuar = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Tente novamente!\nVocê deseja continuar [S/N] ? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{cores["vermelho"]}Infelizmente acabou! :({cores["limpar"]}\n{cores["verde"]}Espero que tenha gostado :D{cores["limpar"]}')
print('Olá')    