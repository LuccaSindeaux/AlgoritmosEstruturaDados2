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

    def radix_sort(self):
        if self.head is None:
            return

        max_valor = self.head.valor
        atual = self.head.proximo
        while atual:
            if atual.valor > max_valor:
                max_valor = atual.valor
            atual = atual.proximo

        exp = 1
        while max_valor // exp > 0:
            buckets = [Lista() for _ in range(10)]

            atual = self.head
            while atual:
                valor_atual = atual.valor
                indice_bucket = (valor_atual // exp) % 10
                # Adiciona o número no balde correspondente
                buckets[indice_bucket].add_valor(valor_atual)
                atual = atual.proximo


            self.head = None 
            self.tail = None

            for bucket in buckets:
                if bucket.head:
                    if self.head is None:
                        self.head = bucket.head
                        self.tail = bucket.tail
                    else:
                        self.tail.proximo = bucket.head
                        bucket.head.anterior = self.tail
                        self.tail = bucket.tail
            
            exp *= 10
        
    def __str__(self):
        if self.head is None:
            return "[]"

        numeros_formatados = []
        atual = self.head
        while atual is not None:
            numeros_formatados.append(f"{atual.valor:02d}")
            atual = atual.proximo

        conteudo_da_string = ",".join(numeros_formatados)
        return f"[{conteudo_da_string}]"

    def imprime_lista(self):
        if self.head is None:
            print("A lista está vazia.")
            return
        
        atual = self.head
        while atual is not None:
            print(f"Valor: {atual.valor}")
            atual = atual.proximo




dados_sorteios = [
    {'concurso': 2683, 'numeros': [57, 1, 27, 47, 3, 23]},
    {'concurso': 2667, 'numeros': [8, 4, 51, 46, 21, 1]},
    {'concurso': 2700, 'numeros': [11, 28, 48, 1, 19, 20]},
    {'concurso': 2675, 'numeros': [31, 1, 45, 26, 34, 42]}
]

print("Números Sorteados. - Sorteio")

for sorteio in dados_sorteios:
    lista_do_sorteio = Lista()
    
    for numero in sorteio['numeros']:
        lista_do_sorteio.add_valor(numero)

    lista_do_sorteio.radix_sort()

    print(f"{lista_do_sorteio} - {sorteio['concurso']}")