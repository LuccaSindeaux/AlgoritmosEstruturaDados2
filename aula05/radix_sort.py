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
    {'concurso': 2785, 'numeros': [10, 22, 31, 40, 51, 58]},
    {'concurso': 2784, 'numeros': [9, 15, 25, 29, 33, 48]},
    {'concurso': 2783, 'numeros': [7, 18, 20, 26, 36, 59]},
    {'concurso': 2782, 'numeros': [3, 11, 21, 23, 40, 52]},
    {'concurso': 2781, 'numeros': [6, 16, 26, 32, 46, 55]},
    {'concurso': 2780, 'numeros': [1, 2, 23, 30, 45, 54]},
    {'concurso': 2779, 'numeros': [10, 19, 39, 41, 43, 57]},
    {'concurso': 2778, 'numeros': [5, 25, 29, 30, 43, 47]},
    {'concurso': 2777, 'numeros': [13, 22, 25, 27, 42, 47]},
    {'concurso': 2776, 'numeros': [1, 10, 19, 23, 27, 49]},
    {'concurso': 2775, 'numeros': [17, 26, 45, 46, 48, 53]},
    {'concurso': 2774, 'numeros': [8, 18, 26, 27, 47, 50]},
    {'concurso': 2773, 'numeros': [2, 17, 22, 42, 49, 52]},
    {'concurso': 2772, 'numeros': [10, 11, 12, 19, 23, 47]},
]

print("Números Sorteados.  - Sorteio")

for sorteio in dados_sorteios:
    lista_do_sorteio = Lista()
    
    for numero in sorteio['numeros']:
        lista_do_sorteio.add_valor(numero)

    lista_do_sorteio.radix_sort()

    print(f"{lista_do_sorteio} - {sorteio['concurso']}")