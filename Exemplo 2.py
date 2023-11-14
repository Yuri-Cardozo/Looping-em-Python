
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

i = 1
while i <= 5:
    print("Coloque a quantidade de votos para o dia {i}: ")
    votos = int(input())

    if i == 1:
        segunda = votos
    elif i == 2:
        terca = votos
    elif i == 3:
        quarta = votos
    elif i == 4:
        quinta = votos
    elif i == 5:
        sexta = votos

    i += 1

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia  Decidido foi segunda-feira.")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia  Decidido foi terça-feira.")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia decidido  foi quarta-feira.")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia  decidido  foi quinta-feira.")
else:
    print("O dia decidido foi sexta-feira.")
