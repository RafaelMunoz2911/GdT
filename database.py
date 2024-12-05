import sqlite3

conn = sqlite3.connect('gdt.db')

#-----------criar tabelas funcionarios

conn.execute('CREATE TABLE funcionarios(\
                id INTEGER PRIMARY KEY,\
                chapa TEXT,\
                nome TEXT,\
                cpf TEXT,\
                rg TEXT,\
                data_nascimento TEXT,\
                rais TEXT,\
                cidade TEXT,\
                bairro TEXT,\
                endereco TEXT,\
                cep TEXT,\
                telefone TEXT,\
                pis TEXT,\
                esocial TEXT,\
                sefip TEXT,\
                sindicato TEXT,\
                id_funcao INTEGER REFERENCES funcao(id))')

#-----------criar tabela funcao
 
conn.execute('CREATE TABLE funcao(\
                id INTEGER PRIMARY KEY,\
                descricao TEXT,\
                remuneracao TEXT)')

#-----------criar tabela setor

conn.execute('CREATE TABLE setor(\
                id INTEGER PRIMARY KEY,\
                nome_setor TEXT)')

#-----------criar tabela eventos

conn.execute('CREATE TABLE eventos(\
                id INTEGER PRIMARY KEY,\
                descricao TEXT,\
                id_funcionarios INTEGER REFERENCES funcionarios(id),\
                data_i_even TEXT,\
                data_t_even TEXT)')

print('Banco de Dados criado!')