#exercício_2. Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno Reprovado com média”. Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.

#quatro notas escolares bimestrais de um aluno
#variáveis N1, N2, N3 e N4

n1 = float(input('Favor inserir o valor da nota número 01: '))
n2 = float(input('Favor inserir o valor da nota número 02: '))
n3 = float(input('Favor inserir o valor da nota número 03: '))
n4 = float(input('Favor inserir o valor da nota número 04: '))
md = (n1+n2+n3+n4)/4

if md>5:
    print("Aluno Aprovado com média" , md)
else:
    print("Aluno Reprovado com média" , md)
