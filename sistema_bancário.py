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


def consulta_cadastro(usuario):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM consultas WHERE ID = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()
    
    return (resultado)


def cadastro_cliente():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cpf = input("Digite o seu CPF: ")
        nome = input("Digite o seu Nome: ")
        sobrenome = input("Digite o seu Sobrenome: ")
        telefone = input("Digite o seu Telefone: [+55 xx xxxxx-xxxx] ")
        saldo = 0
        tipo = "Cliente"
        status = "Ativo"

        print(f"Dados para inserção: CPF={cpf}, Nome={nome}, Sobrenome={sobrenome}, Telefone={telefone}, Saldo={saldo}, Tipo={tipo}, Status={status}")

        cursor.execute("INSERT INTO consultas (ID, Nome, Sobrenome, Telefone, Saldo, Tipo, Status) VALUES (?,?,?,?,?,?,?)",(cpf, nome, sobrenome, telefone, saldo, tipo, status))
        conn.commit()
        conn.close()
        return print(f"{nome}, o seu cadastro foi realizado.")
    except sqlite3.Error as error:
        print("Não foi possível realizar o seu cadastro !")
        return None

##administrador

#ativar/desativar cadastro
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
Cliente = consulta_cadastro(usuario)
if Cliente is None:
    cadastrar = input("Deseja se cadastrar ? [S/N]")
    if cadastrar == "S":
        cadastro_cliente()

#verificar cliente ou administrador


##cliente
print(f"Olá {Cliente[1]} {Cliente[2]}")
operacao = input('''
Selecione a opção desejada:
[1] Depósito
[2] Saque
[3] Extrato
[4] Câmbio
[5] Sair
[6] Encerrar conta
''')

#deposito
if operacao == 1:
    deposito = float(input('Digite o valor que deseja depositar: R$ '))

#saque (limite de saque)
elif operacao == 2:
    saque = float(input('Digite o valor que deseja Sacar: R$ '))

#extrato
elif operacao == 3:
    print("Extrato do cliente")

#conveter em outras moedas
elif operacao == 4:
    print("Calculadora de Câmbio")

#sair do sistema
elif operacao == 5:
    print("sistema encerrado, até mais!")

#encerrar conta
elif operacao == 6:
    print("Por favor, procure o Administrador")
