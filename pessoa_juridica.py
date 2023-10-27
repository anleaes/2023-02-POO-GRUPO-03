from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, email, cnpj):
        super().__init__(nome, email)
        self.cnpj = cnpj

    def __str__(self):
        return super().__str__() + f", CNPJ: {self.cnpj}"