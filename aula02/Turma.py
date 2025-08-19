class Turma:
    def __init__(self):
        self.alunos = []

    def inserir_alunos(self, nome, matricula, nota):
        novo_aluno = {"matricula": matricula, "nome": nome, "nota": nota}
        self.alunos.append(novo_aluno)
        print(f"Aluno {nome} inserindo com sucesso!\n")

    def status_aluno(self, nota):
        return "Aprovado" if nota >= 6 else "Reprovado"

    def ordenar_por_matricula(self):
        self.alunos.sort(key = lambda x: x["matricula"])
        print("\nAlunos ordenados por matrícula: ")
        for aluno in self.alunos:
            print(f"{aluno['nome']} - matricula: {aluno['matricula']}")
    
    def ordenar_por_nota(self):
        self.alunos.sort(key=lambda x: x["nota"], reverse=True)
        print("\nAlunos ordenados por nota (maior para menor):")
        for aluno in self.alunos:
            print(f"{aluno['nome']} - Nota: {aluno['nota']}")

#Busca binária
    def busca_binaria(alunos, matricula):
        inicio = 0
        fim = len(alunos) - 1
        comparacoes = 0

        while inicio <= fim:
            meio = (inicio + fim) // 2
            comparacoes += 1
            if alunos[meio]["matricula"] == matricula:
                return alunos[meio], comparacoes
            elif alunos[meio]["matricula"] < matricula:
                inicio = meio + 1
            else:
                fim = meio - 1
        return None, comparacoes

    def exibir_resultado(self, aluno, comparacoes):
        if aluno:
            print(f"\nAluno encontrado após {comparacoes} comparações:")
            print(f"Nome: {aluno['nome']}")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nota: {aluno['nota']}")
            print(f"Status: {self.status_aluno(aluno['nota'])}")
        else:
            print(f"\nAluno não encontrado após {comparacoes} comparações.")

    def inserir_aluno(self):
        nome = input("Nome do aluno: ")
        matricula = int(input("Matrícula: "))
        nota = float(input("Nota: "))
        novo_aluno = {"matricula": matricula, "nome": nome, "nota": nota} #{} -> Criação de um dicionário
        self.alunos.append(novo_aluno)
        print(f"Aluno {nome} inserido com sucesso!\n")

    def buscar_por_nome(self, nome_busca):
        encontrados = []
        comparacoes = 0

        for aluno in self.alunos:
            comparacoes += 1
            if aluno["nome"].lower() == nome_busca.lower():
                encontrados.append(aluno)

        return encontrados, comparacoes


    def exibir_resultado_nome(self, encontrados, comparacoes):
        if encontrados:
            print(f"\n{len(encontrados)} aluno(s) encontrado(s) após {comparacoes} comparações:")
            for aluno in encontrados:
                print(f"Nome: {aluno['nome']}")
                print(f"Matrícula: {aluno['matricula']}")
                print(f"Nota: {aluno['nota']}")
                print(f"Status: {self.status_aluno(aluno['nota'])}")
                print("---")
        else:
            print(f"\nNenhum aluno encontrado após {comparacoes} comparações.")