from pessoa import Pessoa
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
from curso import Curso
from incricao import Inscricao

if __name__ == "__main__":
    curso_python = Curso("Python para iniciantes", "2 months")

    pessoa_fisica = PessoaFisica("João", "joao@email.com", "123.456.789-01")
    pessoa_juridica = PessoaJuridica("Empresa XYZ", "contato@empresa.com", "12.345.678/0001-90")

    inscricao = Inscricao()

    # Realizando inscrições
    inscricao.realizar_inscricao(pessoa_fisica, curso_python)
    inscricao.realizar_inscricao(pessoa_juridica, curso_python)