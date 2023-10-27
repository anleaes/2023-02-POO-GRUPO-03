from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, email, cpf):
        super().__init__(nome, email)
        self.cpf = cpf

    def __str__(self):
        return super().__str__() + f", CPF: {self.cpf}"