'''
Neste exercício é usado uma lista encadeada, portanto, cada elemento possui um endereço de memória,
NÃO sendo possível dividir a lista ao meio, a busca não pode ser binária, e deve ser obrigatoriamente uma BUSCA SEQUENCIAL.
'''

class NoAluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        self.proximo = None


class TurmaEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def inserir_aluno(self, nome, matricula, nota):
        novo = NoAluno(nome, matricula, nota)
        if not self.inicio:
            self.inicio = novo
            self.final = novo
        else:
            self.final.proximo = novo
            self.final = novo
        print(f"Aluno {nome} inserido com sucesso!\n")

    def busca_sequencial_nome(self, nome_busca):
        atual = self.inicio
        encontrados = []
        comparacoes = 0

        while atual:
            comparacoes += 1
            if atual.nome.lower() == nome_busca.lower():
                encontrados.append(atual)
            atual = atual.proximo

        return encontrados, comparacoes

    def busca_sequencial_matricula(self, matricula_busca):
        atual = self.inicio 
        comparacoes = 0

        while atual:
            comparacoes += 1
            if atual.matricula == matricula_busca:
                return atual, comparacoes
            atual = atual.proximo
        return None, comparacoes

    def ordenar_por_nota(self):
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


def status_aluno(nota):
    return "Aprovado" if nota >= 6 else "Reprovado"


def exibir_resultado(aluno, comparacoes):
    if aluno:
        print(f"\nAluno encontrado após {comparacoes} comparações:")
        print(f"Nome: {aluno.nome}")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Nota: {aluno.nota}")
        print(f"Status: {status_aluno(aluno.nota)}")
    else:
        print(f"\nAluno não encontrado após {comparacoes} comparações.")


def exibir_resultado_nome(encontrados, comparacoes):
    if encontrados:
        print(f"\n{len(encontrados)} aluno(s) encontrado(s) após {comparacoes} comparações:")
        for aluno in encontrados:
            print(f"Nome: {aluno.nome}")
            print(f"Matrícula: {aluno.matricula}")
            print(f"Nota: {aluno.nota}")
            print(f"Status: {status_aluno(aluno.nota)}")
            print("---")
    else:
        print(f"\nNenhum aluno encontrado após {comparacoes} comparações.")


def main():
    turma = TurmaEncadeada()

    # Alunos iniciais
    turma.inserir_aluno("Ana", 1001, 8.5)
    turma.inserir_aluno("Bruno", 1002, 5.0)
    turma.inserir_aluno("Carla", 1003, 6.7)
    turma.inserir_aluno("Daniel", 1004, 9.2)
    turma.inserir_aluno("Eduarda", 1005, 4.8)

    while True:
        print("\n--- MENU ---")
        print("1. Buscar aluno por matrícula")
        print("2. Inserir novo aluno")
        print("3. Ordenar alunos por nota")
        print("4. Buscar aluno por nome")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            matricula_busca = int(input("Digite a matrícula: "))
            aluno, comparacoes = turma.busca_sequencial_matricula(matricula_busca)
            exibir_resultado(aluno, comparacoes)

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            matricula = int(input("Matrícula: "))
            nota = float(input("Nota: "))
            turma.inserir_aluno(nome, matricula, nota)

        elif opcao == "3":
            turma.ordenar_por_nota()
            print("\nAlunos ordenados por nota (maior para menor):")
            atual = turma.inicio
            while atual:
                print(f"{atual.nome} - Nota: {atual.nota}")
                atual = atual.proximo

        elif opcao == "4":
            nome_busca = input("Digite o nome do aluno: ")
            encontrados, comparacoes = turma.busca_sequencial_nome(nome_busca)
            exibir_resultado_nome(encontrados, comparacoes)

        elif opcao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


