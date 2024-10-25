from services.aluno_services import AlunoService
from repositories.aluno_repository import AlunoRepository
from config.connection import Session

def main(): 
    session = Session()
    repository = AlunoRepository(session)
    service = AlunoService(repository)
     
    service.criar_aluno()

    print("\nListando todos os alunos.")
    alunos = service.listar_todos_alunos()

    for aluno in alunos:
        print(f"R.A.: {aluno.ra} - Nome: {aluno.nome} - Sobrenome: {aluno.sobrenome} - E=mail: {aluno.email}")

if __name__ == "__main__":
    main()