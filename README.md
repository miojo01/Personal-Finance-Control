#💰 Sistema de Controle de Finanças Pessoais
Este projeto é um sistema simples para gerenciar suas finanças pessoais, permitindo o registro de receitas e despesas, cálculo do saldo, conversão de moedas via API externa e geração de relatórios gráficos. Foi desenvolvido utilizando conceitos de Programação Orientada a Objetos (POO) em Python.

##🎯 Objetivo
Criar uma aplicação modular e organizada para controlar o fluxo financeiro pessoal, aplicando os principais conceitos da POO:

✅ Classes e Objetos
✅ Herança
✅ Polimorfismo (sobreposição de métodos)
✅ Sobrecarga de métodos (construtores com parâmetros diferentes)

##🛠 Tecnologias Utilizadas
- Python 3
- Bibliotecas Python: pandas, matplotlib, requests
- API externa de câmbio: Frankfurter.app

##📁 Estrutura do Projeto
Controle de Finanças/
├── transacao.py       # Classes Transacao, Receita, Despesa
├── carteira.py        # Classe para gerenciar as transações
├── cambio_api.py      # Função para conversão de moedas via API
├── relatorio.py       # Geração de relatórios e gráficos
├── main.py            # Arquivo principal que executa o programa
└── README.md          # Documentação do projeto

##🔧 Funcionalidades
Registrar receitas e despesas com descrição, valor e data.
Calcular o saldo atual.
Converter o saldo para outra moeda utilizando API externa.
Gerar relatório CSV com o histórico financeiro.
Criar gráficos de resumo de receitas e despesas.

##🧠 Conceitos de POO Aplicados
Classes e Objetos: Representação das transações financeiras.
Herança: Classes Receita e Despesa herdam de Transacao.
Polimorfismo: Método mostrar() sobrescrito nas subclasses para exibir informações específicas.
Sobrecarga: Implementação de construtores com parâmetros diferentes para flexibilizar criação de objetos.

##👨‍💻 Autoria
Desenvolvido por Leonardo S. Batschauer Estudante de Análise e Desenvolvimento de Sistemas no IFSC
