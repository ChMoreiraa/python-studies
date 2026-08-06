import random

nomes = []
for i in range(4):
    nome = input(f"{i + 1}° Aluno: ")
    nomes.append(nome)

print(f"O aluno escolhido foi {random.choice(nomes)}")