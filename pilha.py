#Definir a classe Pilha que encapsula as operações de um pilha 
class Pilha:
    #Inicializar a pilha com um lista vazia
    def __init__(self):
        self.itens = []
    
    #Verificar se a pilha esta vazia
    def pilha_vazia(self):
        return len(self.itens) == 0
    
    def empilhar (self, item):
        self.itens.append(item)
        print(f"Empilhar: {item} | Pilha Atial: {self.itens}") 

    def desenpilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia. Não é possivel desempilhar.")
            return None
        item = self.itens.pop()# pop tira o ultimo numero da pilha 
        print(f"Empilhado: {item} | Pilha atual: {self.itens}")

        return item
    
    def topo(self):
        if self.pilha_vazia():
            print("A pilha está vazia, Não há topo.")
            return None
        return self.itens [-1] # -1 vai para o final a pilha
    
    #Empilhar/Desenpilhar os valores [5, 10, 20, 25]
def exec_pilha():
    pilha = Pilha()

    print(f"A pilha está vazia? {pilha.pilha_vazia()}")

    #Empilhar
    pilha.empilhar(5)
    pilha.empilhar(10)
    pilha.empilhar(15)
    pilha.empilhar(20)
    pilha.empilhar(25)

    print(f"Item no tepo da pilha: {pilha.topo()}")

    #Desempilhar
    pilha.desenpilhar()

    print(f"Item no topo após desenpilhar:{pilha.topo()}")

    pilha.desenpilhar()
    pilha.desenpilhar()
    pilha.desenpilhar()
    pilha.desenpilhar()

exec_pilha()