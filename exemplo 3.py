soma_impar = 0
print("***VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES***")

for x in range (1,50,2):
    impar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    soma_impar = soma_impar + impar
print("A média de nota dos alunos ímpares foi {}". format(soma_impar/25))

soma_par = 0
print("***VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES***")
for x in range (2,51,2):
    par = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    soma_par = soma_par + par
print("A média de nota dos alunos pares foi {}". format(soma_par/25))

if soma_impar > soma_par:
    print("Os alunos de número ímpar tiveram a maior nota")
elif soma_par > soma_impar:
    print("Os alunos de número par tiveram a maior nota")
else:
    print("HOUVE UM EMPATE!!!")
