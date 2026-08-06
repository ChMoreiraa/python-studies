from random import shuffle

nomes = []
for i in range(4):
    nome = input(f"{i + 1}° Aluno: ")
    nomes.append(nome)

shuffle(nomes)
print(f"A ordem de apresentação será \n{nomes}")