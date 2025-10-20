import os

class No:
    """
    Representa um nó na árvore do sistema de arquivos.
    Pode ser um arquivo ou uma pasta.
    """
    def __init__(self, nome, tipo):
        """
        Inicializa o nó.
        
        Args:
            nome (str): Nome do arquivo ou pasta.
            tipo (str): "arquivo" ou "pasta".
        """
        self.nome = nome
        self.tipo = tipo  # "arquivo", "pasta" ou "erro"
        self.filhos = []

    def adicionar_filho(self, filho):
        """Adiciona um nó filho (usado apenas se o tipo for "pasta")."""
        if self.tipo == "pasta":
            self.filhos.append(filho)

    def imprimir(self, nivel=0):
        """
        Imprime recursivamente o nó e seus filhos com indentação
        para representar a hierarquia.
        """
        # Define a indentação com base no nível da árvore
        # " |  " * nivel cria a estrutura de galhos
        indentacao = "|  " * nivel
        
        # O prefixo do item
        prefixo = "|- "
        
        # A raiz (nível 0) é impressa sem indentação ou prefixo
        if nivel == 0:
            print(f"{self.nome} ({self.tipo})")
        else:
            print(f"{indentacao}{prefixo}{self.nome} ({self.tipo})")

        # Ordena os filhos para exibição: pastas primeiro, depois arquivos,
        # ambos em ordem alfabética.
        filhos_ordenados = sorted(self.filhos, key=lambda x: (x.tipo, x.nome))

        # Chamada recursiva para cada filho
        for filho in filhos_ordenados:
            filho.imprimir(nivel + 1)

class Arvore:
    """
    Representa a estrutura de diretórios completa como uma árvore
    e gerencia sua construção e exibição.
    """
    def __init__(self, caminho_raiz):
        """
        Inicializa a árvore. O caminho raiz é validado e
        o método ler_diretorio é chamado para construir a árvore.
        """
        if not os.path.isdir(caminho_raiz):
            print(f"Erro: Caminho '{caminho_raiz}' não é um diretório válido.")
            self.raiz = None
        else:
            # A construção da árvore começa aqui
            self.raiz = self.ler_diretorio(caminho_raiz)

    def ler_diretorio(self, caminho):
        """
        Método recursivo que lê um caminho do sistema de arquivos e
        retorna um nó (No) correspondente, com todos os seus descendentes.
        """
        # Ignora caminhos que não existem (ex: links simbólicos quebrados)
        if not os.path.exists(caminho):
            return None

        # Pega o nome base do caminho (ex: 'documentos' de '/home/user/documentos')
        nome = os.path.basename(caminho)

        # Caso Base 1: É um arquivo
        if os.path.isfile(caminho):
            return No(nome, "arquivo")

        # Caso Recursivo: É um diretório
        if os.path.isdir(caminho):
            no_pasta = No(nome, "pasta")
            
            try:
                # Tenta listar os itens dentro da pasta
                itens = os.listdir(caminho)
            except PermissionError:
                # Se houver erro de permissão, adiciona um nó de erro e para
                no_pasta.adicionar_filho(No("[Acesso Negado]", "erro"))
                return no_pasta
            except FileNotFoundError:
                 # Se o diretório for excluído durante a varredura
                return None

            # Para cada item na pasta, faz a chamada recursiva
            for item_nome in itens:
                item_caminho = os.path.join(caminho, item_nome)
                
                # Chamada recursiva
                no_filho = self.ler_diretorio(item_caminho)
                
                # Adiciona o filho se ele for válido (não for None)
                if no_filho:
                    no_pasta.adicionar_filho(no_filho)
            
            return no_pasta
        
        # Ignora outros tipos de arquivos (sockets, pipes, etc.)
        return None

    def imprimir(self):
        """Imprime a estrutura da árvore a partir da raiz."""
        if self.raiz:
            print(f"Exibindo estrutura para: {self.raiz.nome}")
            print("-" * 30)
            self.raiz.imprimir()
            print("-" * 30)
        else:
            print("A árvore está vazia ou não pôde ser construída.")

# --- Execução Principal do Programa ---
if __name__ == "__main__":
    print("--- Construtor de Árvore de Diretórios ---")
    
    # Continua pedindo um caminho até que um válido seja fornecido
    while True:
        caminho_input = input("Digite o caminho do diretório (ou 'sair'): ")
        
        if caminho_input.lower() == 'sair':
            break

        # Verifica se o caminho é um diretório válido
        if not os.path.isdir(caminho_input):
            print(f"\nErro: O caminho '{caminho_input}' não existe ou não é um diretório.")
            print("Por favor, tente novamente.\n")
        else:
            try:
                # 1. Instancia a Árvore (que chama ler_diretorio na inicialização)
                arvore_diretorio = Arvore(caminho_input)
                
                # 2. Imprime a árvore construída
                arvore_diretorio.imprimir()
                
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
            
            # Sai do loop após a execução bem-sucedida
            break