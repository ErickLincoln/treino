#exercício_5. Primeiro, execute a atribuição:
#palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca'] 
#Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a primeira e a última palavra, na ordem do dicionário. 

print("\n######################\n")
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca'] #lista criada
print('Da lista: ',palavras)

palavras.sort() #A função 'sort'  ordena a lista em ordem alfabética
print('A primeira palavra:' , palavras[0]) #utilizei '[0]' para retornar o primeiro indice
palavras.sort(reverse = True) #A função 'sort' 
#com a opção 'reverse = True' ordena a lista em ordem alfabética reversa
print('A última palavra:' , palavras[0]) #utilizei '[0]' para retornar o primeiro indice
print('Segundo a ordem de dicionário.')
print("\n######################\n")

