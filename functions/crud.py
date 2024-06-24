'''
    Autor: Iago, Rhuan, Katielly, Acassio e Flavia
    Data: 23/06/2024
    Descrição: Classe responsável por salvar os dados no banco de dados.
'''

import sqlite3

#Criando base de dados
connection = sqlite3.connect("dados.db", check_same_thread=False)

#Criando comunicação com base dados
cursor = connection.cursor()

#Criando as tabelas do banco de dados
def create_bd():
    '''
        Função para criar uma tabela no banco de dados
    '''
    cursor.execute("create table aluno (ano integer, nome text)")
    cursor.execute("create table perguntas (pergunta text, resposta text, sentimento text)")
    cursor.execute("create table sensores (ultrassonico real, bt_verde integer, bt_vermelho integer, temperatura real)")
    connection.commit()

#Preenchendo as tabelas do banco de dados
def insert_bd(tabela, dados):
    '''
        Função para inserir valores no banco de dados
    '''
    if(tabela == 'aluno'):
        cursor.execute("insert into aluno values (?,?)", dados)
    elif(tabela == 'perguntas'):
        cursor.execute("insert into perguntas values (?,?,?)", dados)
    elif(tabela == 'sensores'):
        cursor.execute("insert into sensores values (?,?,?,?)", dados)

    connection.commit()

#Lendo as tabelas do banco de dados
def read_bd(tabela):
    '''
        Função para ler valores do banco de dados
    '''
    if(tabela == 'aluno'):
        cursor.execute("select * from aluno")
        row = cursor.fetchall()
        return row[-1]
    elif(tabela == 'perguntas'):
        cursor.execute("select * from perguntas")
        row = cursor.fetchall()
        return row
    elif(tabela == 'sensores'):
        cursor.execute("select * from sensores")
        row = cursor.fetchall()
        return row[-1]