#Converte para Farenheit
def tempFaren (tempCel):
   return ((9/5)*tempCel) + 32

#Converte para Kelvin   
def tempKel (tempCel):
  return (tempCel + 273)

#Entrada em Celsius
tempCel = float(input("Digite o valor em graus Celcils: "))

#Strings
farenheint = tempFaren (tempCel)
kelvin = tempKel (tempCel)

#Mostra na tela
print("O valor em Kelvin é:",kelvin,"; e em Farenheit é:",farenheint,".")
