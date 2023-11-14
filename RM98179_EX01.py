opcao = int(input("Digite: "
    "<b> Basic "
    "<2> Silver "
    "<3> Gold "
    "<4> Platinum"))


while opcao > 0 and opcao < 5:
    faturamento = float(input("Coloque o valor de seu faturamento anual: "))
    if opcao == 1:
        valorBonus = faturamento * (30 / 100)
        nivel = "Basic"
        print("Nivel: ".format(nivel) + "\n" + "Faturamento Anual: ".format(faturamento) + "\n" +
              "Valor Bonus: ".format(valorBonus))
    elif opcao == 2:
        valorBonus = faturamento * (20 / 100)
        nivel = "Silver"
        print("Nivel: {}".format(nivel) + "\n" + "Faturamento Anual: ".format(faturamento) + "\n" +
              "Valor Bonus: {}".format(valorBonus))
    elif opcao == 3:
        valorBonus = faturamento * (10 / 100)
        nivel = "Gold"
        print("Nivel: ".format(nivel) + "\n" + "Faturamento Anual:".format(faturamento) + "\n" +
              "Valor Bonus: ".format(valorBonus))
    elif opcao == 4:
        valorBonus = faturamento * (5 / 100)
        nivel = "Platinum"
        print("Nivel: {}".format(nivel) + "\n" + "Faturamento Anual: ".format(faturamento) + "\n" +
              "Valor Bonus: {}".format(valorBonus))
