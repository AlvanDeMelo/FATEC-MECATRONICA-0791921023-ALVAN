#Guarda a somatória dos valores informados
somatoria = 0
#Conta a quantidade de valores informados
contador = 0
#Guarda o maior valor informado
maior = 0
#Guarda o menor valor informado
menor = 0
#Constrói a lógica de repetição - enquanto se mantiver verddaeiro, repete o código
continuar = True
while continuar == True:
  valor = int(input("Valor:"))
  #Adiciona o valor na somatória
  somatoria += valor #somatoria = somatória + valor
  #Adiciona mais um na contagem
  contador += 1 #contador = contador + 1
  #Para verificar se é oprimeiro numero informado
  if contador == 1:
    maior = valor
    menor = valor
  else:
    if valor > maior:
      maior = valor
    elif valor < menor:
      menor = valor
  #Verifica se o usuário deseja continuar
  continuar = input("Continuar?") == 's'

media = somatoria/contador
print("Media:", media)
print("Maior:", maior)
print("Menor:", menor)
