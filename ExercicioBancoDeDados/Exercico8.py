Exercico8.py

import sqlite3

# Função para criar as tabelas
def criar_tabelas():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    # Criar tabela "clientes"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT
        )
    ''')

    # Criar tabela "compras"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            produto TEXT,
            valor REAL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')

    conn.commit()
    conn.close()

# Função para inserir dados nas tabelas
def inserir_dados():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    # Inserir dados nas tabelas
    cursor.executemany('''
        INSERT INTO clientes (id, nome) VALUES (?, ?)
    ''', [(1, 'Cliente A'), (2, 'Cliente B'), (3, 'Cliente C')])

    cursor.executemany('''
        INSERT INTO compras (id, cliente_id, produto, valor) VALUES (?, ?, ?, ?)
    ''', [(1, 1, 'Produto X', 50.00), (2, 2, 'Produto Y', 30.00), (3, 3, 'Produto Z', 25.00)])

    conn.commit()
    conn.close()

# Função para realizar a consulta
def consultar_dados():
    conn = sqlite3.connect('exemplo.db')
    cursor = conn.cursor()

    # Consulta para exibir o nome do cliente, o produto e o valor de cada compra
    cursor.execute('''
        SELECT
            c.nome AS NomeCliente,
            co.produto AS Produto,
            co.valor AS Valor
        FROM
            compras co
            JOIN clientes c ON co.cliente_id = c.id
    ''')

    # Imprimir o resultado da consulta
    for row in cursor.fetchall():
        print(row)

    conn.close()

# Chamando as funções
criar_tabelas()
inserir_dados()
consultar_dados()
