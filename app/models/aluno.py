from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base()

class Aluno(Base):
    # Definindo características da tabela.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ra = Column(String(250), unique=True)
    nome = Column(String(250))
    sobrenome = Column(String(250))
    email = Column(String(250), unique=True)
    senha = Column(String(250))

    # Definindo atributos da classe
    def __init__(self,ra: str, nome: str, sobrenome: str, email: str, senha: str)-> None:
        self.ra = ra
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
