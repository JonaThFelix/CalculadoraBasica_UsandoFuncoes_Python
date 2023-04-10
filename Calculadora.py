# ---------------------- MENU DAS FUNÇÕES ---------------------#
#função de soma
def somar(x,y):
  return x + y
  
#função de subtração
def subtrair(x,y):
  return x - y

#função de divisão
def dividir(x,y):
  return x / y

#função de multiplicação
def multiplicar(x,y):
  return x * y
# -------------------------------------------------------------#


#menu apenas para mostrar na tela as opções
print('Selecione: \n')
print('1: ------- SOMAR')
print('2: ------- SUBTRAIR')
print('3: ------- DIVIDIR')
print('4: ------- MULTIPLICAR\n')

#a escolha do menu definirá a ação do if
escolha = int(input('Digite: '))

if escolha == 1:
  x = int(input('Digite o primeiro valor: '))
  y = int(input('Digite o outro valor: '))
  print(f'O resultado é {somar(x,y)} .') #apenas chamo a função (+), ora declarada

if escolha == 2:
  x = int(input('Digite o primeiro valor: '))
  y = int(input('Digite o outro valor: '))
  print(f'O resultado é {subtrair(x,y)} .') #apenas chamo a função (-), ora declarada

if escolha == 3:
  x = int(input('Digite o primeiro valor: '))
  y = int(input('Digite o outro valor: '))
  print(f'O resultado é {dividir(x,y)} .') #apenas chamo a função (/), ora declarada

if escolha == 4:
  x = int(input('Digite o primeiro valor: '))
  y = int(input('Digite o outro valor: '))
  print(f'O resultado é {multiplicar(x,y)} .') #apenas chamo a função (*), ora declarada