class Item:
    def __init__(self, nome: str, valor: int):
        self.nome = nome
        self.valor = valor

    def __repr__(self):
        return f'Item({self.nome}, {self.valor})'

class Carrinho:
    def  __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    @property
    def valor(self):
        return sum(map(lambda item: item.valor, self.itens))


class Promocao10:
    def __init__(self, next=None):
        self.next = next

    def calcular(self, carrinho: Carrinho):
        if carrinho.valor > 1_000:
            return carrinho.valor - (carrinho.valor * 0.1)

        if self.next:
            return  self.next.calcular(carrinho)

class Promocao5:
    def __init__(self, next=None):
        self.next = next

    def calcular(self, carrinho: Carrinho):
        if len(carrinho.itens) >= 5:
            return carrinho.valor - (carrinho.valor * 0.05)

        if self.next:
            return  self.next.calcular(item)

class Promocoes:
    def calcular(self, valor):
        return Promocao10(Promocao5()).calcular(valor)


c = Carrinho()
p = Promocoes()
c.adicionar_item(Item('Xiaomi', 2000))
c.adicionar_item(Item('LG', 1000))
c.adicionar_item(Item('Motorola', 1050))
c.adicionar_item(Item('Samsung', 3000))

print("Valor sem promoção: ", c.valor)
print("Valor com promoção:", p.calcular(c))