from transacao import Transacao, Receita, Despesa, ReceitaExtra

class Carteira:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao):
        self.transacoes.append(transacao)

    def saldo(self):
        total = 0
        for t in self.transacoes:
            if isinstance(t, Receita):
                total += t.valor
            else:
                total -= t.valor
        return total

    def listar(self):
        for t in self.transacoes:
            print(t.mostrar())
