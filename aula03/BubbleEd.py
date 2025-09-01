class Node:
    def __inti_(self, number):
        self.value = number
        self.next = None

class List: 
    def __init__(self):
        self.head = None
        self.tail = None

    
    def addValue(self, value):
        novo_no = Node(value)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no

        if self.head is None:
            pass

    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            no_atual = self.head
            while no_atual is not None:
                print(f"Valor: {no_atual.valor}")
                no_atual = no_atual.next

    #Vai sempre até o final
    def ordenaBubble(self):
        if self.head is None or self.head.next is None:
            return
        trocou = True
        while trocou:
            trocou = False
            atual = self.head

            while atual.next is not None:
                proximo = atual.next
                if atual.value > proximo.value:
                    atual.value, proximo.value = proximo.value, atual.value
                    trocou = True
                atual = atual.next
    
    #Define um final, tendo menos "passagens"
    def ordena_bubble(self):
        if self.head is None or self.head.next is None:
            return
    
        fim = None
    
        while fim != self.head:
            atual = self.head
            trocou = False
    
            while atual.next != fim:
                proximo = atual.next
                if atual.valor > proximo.valor:
                    atual.valor, proximo.valor = proximo.valor, atual.valor
                    trocou = True
                atual = atual.next
    
            fim = atual
    
            if not trocou:
                break