import os

def soma(x,y):
   return print('Resultado:',x+y)

def subtracao(x,y):
    return print('Resultado:',x-y)

def multiplicacao(x,y):
    return print('Resultado:',x*y)

def divisao(x,y):
    return print('Resultado:',x/y)

def porcentagem(x,y):
    z = x * y
    return print('Resultado:',z/100,'%')

opcao = 1


opcao = input('''Selecione a opção desejada:
 1 - Soma
 2 - Subtração
 3 - Multiplicação
 4 - Divisão
 5 - Porcentagem
 0 - Sair''')

if opcao > '0':
    x = int(input('Valor: '))
    y = int(input('Valor: '))
if opcao == '1':
    soma(x,y)
elif opcao == '2':
    subtracao(x,y)
elif opcao == '3':
    multiplicacao(x,y)
elif opcao == '4':
    divisao(x,y)
elif opcao == '5':
    porcentagem(x,y)
elif opcao == '0':
    os.system('cls')
else:
    print('Opção inválida')








