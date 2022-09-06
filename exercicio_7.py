#exercício_7. Utilizando-se de definição de funções. Escreva em python uma função que calcule:
#  O preço de um produto atualizado pela taxa de juros.

#Trata-se de uma função com mais de um parâmetro
def calcula(preço, juros): #criação do escopo da função
    resultado = preço * (1 + (juros / 100)) #definição da função
    print('Preço atualizado do produto: R$', resultado) #retorno da função após ser chamada

calcula(float(input("Insira o valor do produto: R$")), float(input("Insira o valor dos juros: %"))) #chamada de função