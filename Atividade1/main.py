from datetime import date
from pessoa import Pessoa
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
from matricula import Matricula
from aluno import Aluno
from curso import Curso
from incricao import Inscricao

if __name__ == "__main__":

    pessoa_fisica = PessoaFisica(
        "Marcos", "Marcos@gmail.com", "123.456", "Rua A, 123", date(1990, 1, 1))
    print(pessoa_fisica)

    pessoa_juridica = PessoaJuridica("Empresa A", "contato@gmail.com",
                                     "123.456.789/0001-90", "Av. b, 123", "Razao Social ABC", date(2000, 5, 10))
    print(pessoa_juridica)

    curso_python = Curso("Python para iniciantes", "40 horas")
    print(curso_python)

    aluno_joao = Aluno("1", pessoa_fisica)
    print(aluno_joao)

    matricula_joao = Matricula(
        "MOO1", date.today(), curso_python, aluno_joao, pessoa_fisica)
    print(matricula_joao)

    inscricao_joao = Inscricao(
        100.0, date.today(), curso_python, aluno_joao, pessoa_juridica)
    print(inscricao_joao)

    pessoa_fisica.inscrever_curso(curso_python)
