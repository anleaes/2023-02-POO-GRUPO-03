from categoria import Categoria
from produto import Produto
from ordem_item import OrdemItem
from ordem import Ordem
from cliente import Cliente
from cliente_socialnetwork import ClienteSocialnetwork
from socialnetwork import Socialnetwork

categoria1 = Categoria(id=1, nome="Eletronico",
                       descricao="Dispositivos Eletronicos")

produto1 = Produto(nome="Laptop", descricao="Otimo Laptop",
                   data_fabricacao="01-01-2023", ativo=True, categoria=categoria1)

cliente1 = Cliente(primeiro_nome="Rodrigo", ultimo_nome="Morini", endereco="123 Brasil",
                   numero_celular="123456", email="rodrigo@gmail.com", genero="Homem")

ordem1 = Ordem(preco_total=100, status="Pendente", cliente=cliente1)

socialnetwork1 = Socialnetwork(nome="Facebook", descricao="Midia Social")

clientesocialnetwork1 = ClienteSocialnetwork(
    cliente=cliente1, socialnetwork=socialnetwork1)

print(f"Nome do Produto: {produto1.nome}")
print(f"Nome do Cliente: {cliente1.primeiro_nome} {cliente1.ultimo_nome}")
print(f"Midia Socialll: {clientesocialnetwork1.socialnetwork.nome}")
