#exercício_6. Utilizando-se de definição de funções. Escreva em python uma função que
# calcule F(X):
#sendo:
#F(X) = X² + 1

def f(x): #definindo uma função
    resultado = x**2 + 1
    print('F(x) =', resultado)

f(int(input("Insira o valor de X: "))) #chamada de função
