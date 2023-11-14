minutos_atuais = int(input("Digite os minutos atuais: "))
senha = "LIBERDADE"
if minutos_atuais > 5:
    senha = "LIBERDADE120"

while minutos_atuais > 0:
    resto = minutos_atuais % 10
    senha = str(resto) + senha
    minutos_atuais = minutos_atuais // 10



print("A senha para desbloqueio é:", senha)
