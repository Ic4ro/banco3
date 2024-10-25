from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository

class AlunoService:
    def __init__(self, repository: AlunoRepository):
        self.repository = repository

    def criar_aluno(self)-> None:
        try:
            ra = input ("Digite seu R.A.: ")
            nome = input("Digite seu nome: ")
            sobrenome = input ("Digite seu sobrenome: ")
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            aluno = Aluno(ra=ra, nome=nome, sobrenome=sobrenome , email=email, senha=senha)
            self.repository.salvar_aluno(aluno)
            print("Aluno salvo com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o arquivo: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado{erro}.")

    def listar_todos_alunos(self): 
        return self.repository.listar_todos_alunos()
