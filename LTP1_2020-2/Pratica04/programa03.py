#Pede ao usuário digitar uma senha e valida ela com a senha secreta
#Cria uma variável para perguntar a senha
senha_secreta = "123456"

#Pede para o usuario digitar a sua senha_secreta
senha = input("Informe a senha:")

#Verifica se a senha do usuário está certa
if senha == senha_secreta:
  print("Bem vindo Hakcerman!")

else:
  print("Errooooou!!! :'(")
