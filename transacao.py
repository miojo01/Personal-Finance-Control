from datetime import datetime

class Transacao:
    def __init__(self, valor, descricao, data=None):
        self.valor = valor
        self.descricao = descricao
        self.data = data or datetime.now().strftime("%Y-%m-%d")

    def mostrar(self):
        return f"{self.data} - {self.descricao}: R$ {self.valor:.2f}"
    
class Receita(Transacao):
    def mostrar(self):
        return f"[+] Receita: {super().mostrar()}"

class Despesa(Transacao):
    def mostrar(self):
        return f"[-] Despesa: {super().mostrar()}"

# Sobrecarga com outro tipo de construtor
class ReceitaExtra(Receita):
    def __init__(self, valor, descricao, fonte="Outros"):
        super().__init__(valor, descricao)
        self.fonte = fonte