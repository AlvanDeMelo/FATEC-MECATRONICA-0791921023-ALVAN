#Calculadora Personalizada
#1 - Soma
#2 - Subtração
#3 - Multiplicacao
#4 - Divisao
#5 - R = (V,I)
#6 - V = (R,I)
#7 - I = (V,R)
#8 - Req = Série
#9 - Req = Paralelo
#10 - Potência = (R,I)

def exibir_menu():
  print("Menu Calculadora:")
  print("1 - Somar")
  print("2 - Subtrair")
  print("3 - Multiplicar")
  print("4 - Dividir")
  print("5 - R = (V,I)")
  print("6 - V = (R,I)")
  print("7 - I = (V,R)")
  print("8 - Req = Série")
  print("9 - Req = Paralelo")
  print("10 - Potência = (R,I)")
  print("0 - Sair")

def somar(numero1, numero2):
  return numero1+numero2

def subtrair(numero1, numero2):
  return numero1-numero2

def multiplicar(numero1, numero2):
  return numero1*numero2

def dividir(numero1, numero2):
  if numero2 == 0:
    return "Não existe divisão por zero!"
  else:
   return numero1/numero2

#Programa principal
import os
continuar = True
while continuar == True:
  os.system("clear") #No windows - cls
  exibir_menu()
  opcao = int(input("Opcao:"))
  if opcao == 1:
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    print("Resultado:", somar(n1,n2))
  elif opcao == 2:
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    print("Resultado:", subtrair(n1,n2))
  elif opcao == 3:
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    print("Resultado:", multiplicar(n1,n2))
  elif opcao == 4:
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    print("Resultado:", dividir(n1,n2))
  elif opcao == 5:
    V = float(input("Forneça o valor da tensão:"))
    I = float(input("Forneça o valor da corrente:"))
    print("O valor da resistência é:", dividir(V,I))
  elif opcao == 6:
    R = float(input("Forneça o valor da resistência:"))
    I = float(input("Forneça o valor da corrente:"))
    print("O valor da tensão é:", multiplicar(R,I))
  elif opcao == 7:
    V = float(input("Forneça o valor da tensão:"))
    R = float(input("Forneça o valor da resistência:"))
    print("O valor da tensão é:", dividir(V,R))
  elif opcao == 10:
    R = float(input("Forneça o valor da resistência:"))
    I = float(input("Forneça o valor da corrente:"))
    print("O valor da potência é:", multiplicar(R,I**2))
  elif opcao == 0:
    continuar = False
  else:
    print("Opcao Invalida!")
  input("Pressione enter para continuar")
