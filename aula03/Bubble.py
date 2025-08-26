class No:
    def __init__(self, num):
        self.valor = num
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
    
    def bubbleSort(self):
        lista = []
        atual = self.inicio
        while atual:
            lista.append(atual)
            atual = atual.proximo

        lista.sort(key=lambda x: x.nota, reverse=True)

        for i in range(len(lista) - 1):
            lista[i].proximo = lista[i + 1]
        if lista: 
            lista[-1].proximo = None
            self.inicio = lista[0]
            self.final = lista[-1]

num = [1,5,8,7,65,99,752,114]
lista = Lista(num)
print(lista)