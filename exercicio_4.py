#exercício_4. Escreva expressões algébricas Python correspondentes aos seguintes comandos:

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
print("___(C)____________________________________")
#(c) O número de vezes que 73 cabe em 403.
numsubtraido = 403
subtraidor = 73
quociente = int(numsubtraido/subtraidor)
print("O número de vezes que", subtraidor ,"está em", numsubtraido ,"é" ,quociente , '!')
#nota: Para saber quantas vezes um número cabe dentro de outro, peguemos o número 
# e bata dividir pelo número que queremos saber quantas vezes tal número cabe nele.
#sendo assim: a título de estudos criarei uma versão mais aprofundada(exercicio_4_variação).
print("\n######################\n")
print("___(D)________________________________________")
#(d) O resto de quando 403 é dividido por 73.
divisor = 73
dividendo = 403
resto = dividendo%divisor
print("O resto de", dividendo ,"quando é dividido por", divisor ,"é" ,resto , '!')

print("\n######################\n")
print("___(E)___________________________")
#(e) 2 à 10ª potência.
#número a direita ** número a esquerda
print('O número 2 à 10ª potência é:' , 2**10)

print("\n######################\n")
print("___(F)_________________________________")
#(f) O valor absoluto da distância entre
# a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
#utilizei a função 'ABS' que retorna nada mais do que a distância entre um número e 0 na reta numérica.
sara = 54
mark = 57
absoluto = mark-sara
print('O valor absoluto de entre as alturas de\n Sara(', sara ,'Polegadas) e\n Mark(', mark ,'Polegadas) é =', abs(absoluto),'!')

print("\n######################\n")
print("___(G)_________________________________")
#(g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
preços = (['R$',34.99] , ['R$',29.95], ['R$', 31.50])
print('Dentre os seguintes preços:', list(preços))
#faz-se o uso da função 'MIN' que retorna o menor valor dentro da Tupla
print('O menor preço é:', min(preços))

print("\n######################\n")