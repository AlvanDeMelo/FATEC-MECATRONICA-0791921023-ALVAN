# #operadores de divisão (/) e resto da divisão (%)
# divisão = 15 / 2
# resto = 15 % 2

# print("Divisão:", divisao)
# print("Resto:", resto)

#Ler um número pra ver se par ou ímpar
numero = int(input("Informe um número:"))
#Calcula o resto da divisão por 2
resto = numero % 2
#Olha para o valor do resto
if resto == 0:
  print(numero, 'é par!')
else:
  print(numero, 'é impar!')
