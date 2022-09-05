print("\n######################\n")
# (a) A soma dos 5 primeiros inteiros positivos.
print("___(A)___")
positivos = 1
while (positivos <= 4):
    print(positivos, "+ 1 =" , positivos+1)
    positivos += 1

print("\n######################\n")
#(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
print("___(B)____________________________________________")
sara = 23
mark = 19
fatima = 31
idadeMedia = (sara + mark + fatima)/3
print("A idade média de Sara, Mark e Fátima é de", int(idadeMedia) ,"anos.")

print("\n######################\n")
print("___(C)____________________________________________")
#(c) O número de vezes que 73 cabe em 403.
numsubtraido = 403
subtraidor = 73
quociente = int(numsubtraido/subtraidor)
print("O número de vezes que", subtraidor ,"está em", numsubtraido ,"é" ,quociente , '!')
#nota: Para saber quantas vezes um número cabe dentro de outro, peguemos o número 
# e bata dividir pelo número que queremos saber quantas vezes tal número cabe nele.
#sendo assim: a título de estudos criarei uma versão mais aprofundada(exercicio_4_variação).
