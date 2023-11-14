print("Soma de notas e calculo de médias")

notasPares = 0
notasImpares = 0
mediaGeral = 0.0
mensagem = ""

for linha in range(1, 22, 2):
    notasImpares += float(input("""
Você está inserindo as notas dos alunos cujos números são ímpares.         
 INSIRA A NOTA DO ALUNO DE NÚMERO - {}: """.format(linha)))

for linha in range(2, 22, 2):
    notasPares += float(input("""
Você está inserindo as notas dos alunos cujos números são pares.       
 INSIRA A NOTA DO ALUNO DE NÚMERO - {}: """.format(linha)))

if notasPares > notasImpares:
    mediaGeral = notasPares / 25
    mensagem = """
 média da turma PAR foi {} portanto maior que a impar""".format(mediaGeral)
elif notasImpares > notasPares:
    mediaGeral = notasImpares / 25
    mensagem = """
 média da turma IMPAR foi {} portanto maior que a par""".format(mediaGeral)
else:
    mediaGeral = (notasImpares + notasPares) / 50
    mensagem = """
A média das duas turmas foram iguais - Média {}""".format(mediaGeral)

print(mensagem)