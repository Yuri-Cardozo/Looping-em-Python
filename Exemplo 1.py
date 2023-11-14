assinatura = input("Digite o tipo da sua assinatura: ")
faturamento = float(input("Digite o valor do seu faturamento: "))

if assinatura.upper() == "BASIC":
    bonus = faturamento * 0.3
    print("O valor do bônus a ser pago é de R${}".format(bonus))
elif assinatura.upper() == "SILVER":
        bonus = faturamento * 0.2
        print("O valor do bônus a ser pago é de R${}".format(bonus))
elif assinatura.upper() == "GOLD":
        bonus = faturamento * 0.1
        print("O valor do bônus a ser pago é de R${}".format(bonus))
elif assinatura.upper() == "PLATINUM":
        bonus = faturamento * 0.05
        print("O valor do bônus a ser pago é de R${}".format(bonus))
else:
    print("Assinatura inválida")
