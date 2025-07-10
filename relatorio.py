import matplotlib.pyplot as plt
import pandas as pd
from transacao import Transacao, Receita, ReceitaExtra, Despesa

def gerar_relatorio(transacoes):
    dados = []
    for t in transacoes:
        tipo = "Receita" if isinstance(t, Receita) else "Despesa"
        dados.append([t.data, t.descricao, t.valor, tipo])

    df = pd.DataFrame(dados, columns=["Data", "Descrição", "Valor", "Tipo"])
    df.to_csv("relatorio.csv", index=False)
    print("Relatório gerado: relatorio.csv")

    # Gráfico
    receitas = df[df["Tipo"] == "Receita"]["Valor"].sum()
    despesas = df[df["Tipo"] == "Despesa"]["Valor"].sum()

    plt.bar(["Receitas", "Despesas"], [receitas, despesas], color=["green", "red"])
    plt.title("Resumo Financeiro")
    plt.ylabel("Valor (R$)")
    plt.savefig("grafico.png")
    plt.show()
