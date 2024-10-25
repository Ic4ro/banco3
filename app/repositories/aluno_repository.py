from models.aluno import Aluno
from sqlalchemy.orm import Session

class AlunoRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_aluno(self, aluno: Aluno):
        self.session.add(aluno)
        self.session.commit()
        self.session.refresh()

    def pesquisar_aluno_por_email(self, email: str):
        return self.session.query(Aluno).filter_by(email = email).first()

    def deletar_aluno(self, aluno: Aluno):
        self.session.add(aluno)
        self.session.commit()
        self.session.refresh()   

    def listar_todos_alunos(self): 
        return self.session.query(Aluno).all()