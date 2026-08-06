dias = int(input("Quantos dias alugados? "))
kms = float(input("Quantos Kms rodados? "))
total = (dias * 60) + (kms * 0.15)
print(f"O total a pagar é de R${total:.2f}")