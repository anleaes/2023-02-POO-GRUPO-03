from pessoa import Pessoa


class PessoaJuridica(Pessoa):
    def __init__(self, nome, email, cnpj, endereco, razao_social, data_abertura):
        super().__init__(nome, email, endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data_abertura = data_abertura

    def __str__(self):
        return super().__str__() + f", CNPJ: {self.cnpj}"
