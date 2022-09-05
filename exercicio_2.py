n1 = float(input('Favor inserir o valor da nota número 01: '))
n2 = float(input('Favor inserir o valor da nota número 02: '))
n3 = float(input('Favor inserir o valor da nota número 03: '))
n4 = float(input('Favor inserir o valor da nota número 04: '))
md = (n1+n2+n3+n4)/4

if md>5:
    print("Aluno Aprovado com média" , md)
else:
    print("Aluno Reprovado com média" , md)
