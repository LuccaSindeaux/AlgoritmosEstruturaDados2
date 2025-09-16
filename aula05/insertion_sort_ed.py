import time

class Node:
    def __init__(self, numero):
        self.valor = numero
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_valor(self, valor):
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
            self.tail = novo_no

    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual is not None:
                print(f"Valor: {atual.valor}")
                atual = atual.proximo

#head = [100] -> None / {13} / [200]
#       [200] -> [100]/ {95} / [300]
#       [300] -> [200]/ {119}/ [400]
#       ...
#       [1600] -> [1500]/{146}/None
    def ordena_insertion(self): #13 95 119
        #       13               95
        if self.head is None or self.head.proximo is None:
            return

        atual = self.head.proximo # atual = [200]: proximo endereço de memória
        while atual is not None: # enquanto o atual não for vazio, ou seja, enquanto o endereço de memória possuir um self.proximo
            chave = atual.valor # 95 -> 119 -> 184 ...
            mover = atual.anterior # [100]: endereço de memória
                                    # checa 13 > 95 --> depois do primeiro loop
            while mover is not None and mover.valor > chave: # enquanto mover não for nulo E valor de mover for maior que a chave 
                mover.proximo.valor = mover.valor # 
                mover = mover.anterior

            if mover is None: # se mover for None (na primeira ele será, pois ele é atual.anterior, que no primeiro caso, quando chave for 13, o mover será None)
                self.head.valor = chave # head se torna a chave
            else:
                mover.proximo.valor = chave # se não: o próximo valor depois de "mover" é o valor da próxima chave: 95 no primeiro loop

            atual = atual.proximo # o atual será o próximo valor, neste caso, o 95 que em depois do 13

lista_desordenada = [13, 95, 119, 184, 96, 102, 21]#, 48, 137, 57, 99, 5, 45, 170, 154, 146]
lista = Lista()
for numero in lista_desordenada:
    lista.add_valor(numero)

print("Lista Desordenada:")
lista.imprime_lista()

# inicio = time.time()
lista.ordena_insertion()
# fim = time.time()

print("Lista Ordenada com Insertion Sort:")
lista.imprime_lista()

# print(f"Tempo de execução: {fim - inicio:.6f} segundos")