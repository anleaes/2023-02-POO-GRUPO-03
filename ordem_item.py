from ordem import Ordem
from produto import Produto


class OrdemItem:
    def __init__(self, quantidade, preco_unitario, ordem, produto):
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.ordem = ordem
        self.produto = produto
