from carteira import Carteira
from transacao import Receita, Despesa, ReceitaExtra
from cambio_api import converter
from relatorio import gerar_relatorio

c = Carteira()

# Adicionando dados
c.adicionar(Receita(1000, "Salário"))
c.adicionar(ReceitaExtra(200, "Freelancer", "Upwork"))
c.adicionar(Despesa(300, "Aluguel"))
c.adicionar(Despesa(150, "Mercado"))

# Listar
print("\n--- LISTA DE TRANSAÇÕES ---")
c.listar()

# Saldo
print(f"\nSaldo atual: R$ {c.saldo():.2f}")

# Converter para dólar
print(f"Saldo em dólar: $ {converter(c.saldo()):.2f}")

# Relatório
gerar_relatorio(c.transacoes)
