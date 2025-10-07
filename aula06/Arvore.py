from No import No

class Arvore:
    def __init__(self, raiz = None):
        self.raiz = raiz

    def adicionar_no(self, valor, pai = None):
        novo_no = No(valor)

    def adicionar_ramo(arvore):
        while True:
            arvore.imprimir()
            print("\nEntre com os dados ou ENTER para encerrar!")
            valor = input("Digite o valor/dado a ser inserido: ")
            if not valor:
                break
            
            pai = None
            if not arvore.vazia():
                pai = input("Digite o pai para esse dado: ")
                if not pai:
                    break
            
            arvore.adicionar_no(valor, pai)