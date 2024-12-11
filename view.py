import sqlite3

def connect():
    conn = sqlite3.connect('gdt.db')
    return conn

#-----------funcao para inserir atividade
def insert_funcao(descricao, remuneracao):
    conn=connect()
    conn.execute("INSERT INTO funcao(descricao, remuneracao)\
                VALUES(?, ?)", (descricao, remuneracao))
    
    conn.commit()
    conn.close()

#-----------funcao para inserir funcionario
def insert_funcionario(chapa, nome, cpf, rg, data_nascimento, rais, cidade, bairro, endereco, cep, telefone, id_funcao, pis, esocial, sefip, sindicato):
    conn=connect()
    conn.execute("INSERT INTO funcionarios(chapa, nome, cpf, rg, data_nascimento, rais, cidade, bairro, endereco, cep, telefone, id_funcao, pis, esocial, sefip, sindicato)\
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (chapa, nome, cpf, rg, data_nascimento, rais, cidade, bairro, endereco, cep, telefone, id_funcao, pis, esocial, sefip, sindicato))
    
    conn.commit()
    conn.close()
    
#-----------funcao para gerar contratos
def insert_contrato(descricao, id_funcionarios, data_i_even, data_t_even):
    conn=connect()
    conn.execute("INSERT INTO eventos(descricao, id_funcionarios, data_i_even, data_t_even)\
                VALUES(?, ?, ?, ?)", (descricao, id_funcionarios, data_i_even, data_t_even))
    conn.commit()
    conn.close()
       
#_____teste de funcoes______#
#insert_funcao("Cozinheiro", "169,00")

#insert_funcionario("123", "fulano", "15652786663", "mg2101", "29-11-2002", "caucasiano", "Belo Horizonte", "União", "R.Álvares da Silva, 64", "123456", "123456789", "1", "123456789", "123456", "123456", "123")

#insert_contrato("SEFIP","1", "24-12-2024", "25-12-2024")

