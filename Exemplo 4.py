mnum = int(input("Digite os minutos atuais: "))
cont = num
fator = 1

while cont > 0:
    fator = fator * cont
    cont = cont -1

print("A senha é: LIBERDADE{}". format(fator))
