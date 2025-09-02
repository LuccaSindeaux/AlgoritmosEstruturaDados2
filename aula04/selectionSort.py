'''
O Selection Sort (Ordenação por Seleção) é um algoritmo de ordenação simples que divide a lista em duas partes: uma sublista ordenada que é construída da esquerda para a direita e uma sublista com os itens restantes que ainda não foram ordenados.

O algoritmo funciona da seguinte maneira:
1) Encontra o menor elemento na lista não ordenada.

2) Troca esse menor elemento com o primeiro elemento da lista não ordenada.

3) Move o limite da sublista ordenada um elemento para a direita.

4) Repete os passos até que toda a lista esteja ordenada.
'''

class No:
    def __init__ (self, number):
        self.value = number
        self.next = None

class Lista:
    def __init__ (self):
        self.head = None
        self.tail = None


    def adicionarValor(self, valor):
        novo_no = No(valor)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no

        if self.head is None:
            pass
    
    def imprimir_lista(self):
            elementos = []
            no_atual = self.head
            while no_atual:
                elementos.append(str(no_atual.valor))
                no_atual = no_atual.proximo
            print(" -> ".join(elementos))

    def selectionSort(self):
        if self.head is None or self.head.proximo is None:
            return
        
        no_atual = self.head # nó atual será a cabça da lista

        while no_atual:
            menor_no = no_atual # default-> o nó atual começa como o menor nó
            ponteiro_busca = no_atual.next # o valor depois do nó será o ponteiro comparativo
            while ponteiro_busca:
                if ponteiro_busca.valor < menor_no.valor: # se o valor do ponteiro for maior o valor de seu antecessor
                    menor_no = ponteiro_busca # o menor valor se torna o ponteiro
                ponteiro_busca = ponteiro_busca.next # o ponteiro se torna o próximo valor seguido dele
        
            valor_temp = no_atual.valor
            no_atual.valor = menor_no.valor
            menor_no.valor = valor_temp

            no_atual = no_atual.next