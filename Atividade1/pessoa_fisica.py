from pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, nome, email, endereco, cpf, data_nascimento):
        super().__init__(nome, email, endereco)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def __str__(self):
        return super().__str__() + f", CPF: {self.cpf}"
