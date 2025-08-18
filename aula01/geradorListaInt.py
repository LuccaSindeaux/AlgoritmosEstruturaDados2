'''
Você deverá implementar um algoritmo que execute a mesma função do método index() já implementado na estrutura de dados lista do python.
minha_lista.index(elemento)

Crie uma função que receba como parâmetros uma lista e a informação a ser encontrada
nesta lista.
Esta função deverá retornar a posição da lista onde a informação foi encontrada,
ou retornar None, caso a informação não seja encontrada.
'''

import random

def gerador_lista_inteiros(tamanho_lista: int = 10, intervalo_maximo: int = 50) -> list: 
    return [random.randint(0, intervalo_maximo) for _ in range(tamanho_lista)]

def encontrar_indice(lista_a_buscar: list, elemento_procurado) -> int | None:
    for indice, valor_atual in enumerate(lista_a_buscar):
        if valor_atual == elemento_procurado:
            return indice
    return None

if __name__ == "__main__":
    tamanho = 15
    minha_lista = gerador_lista_inteiros(tamanho_lista=tamanho, intervalo_maximo=100)
    print(f"Lista gerada: {minha_lista}\n")
    elemento_a_encontrar = minha_lista[random.randint(0, tamanho - 1)]
    print(f"--- Procurando pelo elemento: {elemento_a_encontrar} ---")
    
    posicao_encontrada = encontrar_indice(minha_lista, elemento_a_encontrar)
    
    if posicao_encontrada is not None:
        print(f"O elemento {elemento_a_encontrar} foi encontrado na posição {posicao_encontrada}.")
        print(f"Verificação com o método .index(): Posição {minha_lista.index(elemento_a_encontrar)}")
    else:
        print(f"O elemento {elemento_a_encontrar} não foi encontrado.")
        
    print("-" * 40)

    elemento_inexistente = 200 
    print(f"--- Procurando pelo elemento: {elemento_inexistente} ---")
    
    posicao_encontrada = encontrar_indice(minha_lista, elemento_inexistente)

    if posicao_encontrada is not None:
        print(f"O elemento {elemento_inexistente} foi encontrado na posição {posicao_encontrada}.")
    else:
        print(f"O elemento {elemento_inexistente} não foi encontrado (retornou {posicao_encontrada}), como esperado.")