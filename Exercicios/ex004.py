var = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(var))
print("Só tem espaços? ", var.isspace()) #Indica True se for somente espaços
print("É um número? ", var.isnumeric())#True se for um número/numérico , se pode ser convertido
print("É alfabético? ", var.isalpha())#True se for alfabético, somente letras
print("É alfanumérico? ", var.isalnum())# True se conter letras e alfabéto
print("Está em maiúsculas? ", var.isupper())#True se TODAS as letras/caracteres estiverem em maiusculo
print("Está em minúsculas? ", var.islower())#True se TODAS as letras/caracteres estiverem em minusculo
print("Está em capitalizada? ", var.istitle())#True se estiver capitalizada 