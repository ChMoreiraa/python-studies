l = float(input("Largura da parede: "))
h = float(input("Altura da parede: "))

area = l * h
tinta = area / 2
print(f"""Sua parede tem a dimensão de {l}X{h} e sua área é de {area}m².
Para pintar essa parede, você precisará de {tinta}""")