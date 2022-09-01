def remove(self):
    """Remove o elemento que está no topo da pilha."""

    assert self.topo, "Impossível remover valor de pilha vazia."

    self.topo = self.topo.anterior

def insere(self, novo_dado):
    """Insere um elemento no final da pilha."""

    # Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = Nodo(novo_dado)

    # Faz com que o novo nodo seja o topo da pilha.
    novo_nodo.anterior = self.topo

    # Faz com que a cabeça da lista referencie o novo nodo.
    self.topo = novo_nodo

# Cria uma pilha vazia.
pilha = Pilha(int)
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.
for i in range(5):
    Pilha.insere(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

# Remove elementos na pilha.
while pilha.topo != None:
    Pilha.remove()
    print("Removendo elemento que está no topo da pilha: ", pilha)