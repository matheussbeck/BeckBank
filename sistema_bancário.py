import sqlite3
import os

#iniciar banco
db_path = "beckbank.db"
db_path2 = "registro_operacoes.db"

def verificar_e_criar_tabela_consultas():
    try:
        if not os.path.exists(db_path):
            conexao = sqlite3.connect(db_path)
            c = conexao.cursor()
            c.execute('''CREATE TABLE consultas
                            (ID TEXT PRIMARY KEY,
                            Nome TEXT NOT NULL,
                            Sobrenome TEXT NOT NULL,
                            Telefone TEXt,
                            Saldo REAL,
                            Tipo TEXT,
                            Status TEXT)''')
            conexao.commit()
            conexao.close()
            print(f"Banco de dados criado em {db_path}.")
        else:
            conexao = sqlite3.connect(db_path)
            c = conexao.cursor()
            c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='consultas' ''')
            if c.fetchone()[0] == 0:
                c.execute('''CREATE TABLE consultas
                            (ID TEXT PRIMARY KEY,
                            Nome TEXT NOT NULL,
                            Sobrenome TEXT NOT NULL,
                            Telefone TEXt,
                            Saldo REAL,
                            Tipo TEXT,
                            Status TEXT)''')
                conexao.commit()
                print("Tabela 'consultas' criada.")
            conexao.close()
    except sqlite3.Error as error:
        print("Erro ao conectar ao SQLite:", error)


def verificar_e_criar_tabela_operacoes():
    try:
        if not os.path.exists(db_path2):
            conexao = sqlite3.connect(db_path2)
            c = conexao.cursor()
            c.execute('''CREATE TABLE operacoes
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Cliente TEXT NOT NULL,
                            Operacao TEXT NOT NULL
                            )''')
            conexao.commit()
            conexao.close()
            print(f"Banco de dados criado em {db_path2}.")
        else:
            conexao = sqlite3.connect(db_path2)
            c = conexao.cursor()
            c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='operacoes' ''')
            if c.fetchone()[0] == 0:
                c.execute('''CREATE TABLE operacoes
                            (ID TEXT PRIMARY KEY,
                            Nome TEXT NOT NULL,
                            Sobrenome TEXT NOT NULL,
                            Telefone TEXt,
                            Saldo REAL,
                            Tipo TEXT,
                            Status TEXT)''')
                conexao.commit()
                print("Tabela 'operacoes' criada.")
            conexao.close()
    except sqlite3.Error as error:
        print("Erro ao conectar ao SQLite:", error)

##administrador

#cadastrar cliente VIP (sem limite)
#cadastrar administrador
#extrair informacoes de clientes
#extrato de operacoes


#primeiro cadastro é administrador
#tratamento de erros de digitacao
#tratamento erros de cadastro
#tratamento de erros
#horario de funcionamento
#confirmacao de operacoes via telegram


#Sistema Principal

#iniciar banco
verificar_e_criar_tabela_consultas()
verificar_e_criar_tabela_operacoes()
#registro operações

#login digitar dados
usuario = input("Digite o seu CPF: ")
#verificar se os dados existem

#se nao, cadastrar cliente

#verificar cliente ou administrador


##cliente
operacao = input('''
Olá Cliente,
Selecione a opção desejada:
[1] Depósito
[2] Saque
[3] Extrato
[4] Câmbio
[5] Sair
[6] Encerrar conta
''')

#deposito
#saque (limite de saque)
#conveter em outras moedas
#extrato
#encerrar conta