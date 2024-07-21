# banco_de_dados.py

import sqlite3

# Função para conectar ao banco de dados e criar uma tabela
def criar_tabela():
    # Conectar ao banco de dados (ou criar o banco se não existir)
    conn = sqlite3.connect('meu_banco_de_dados.db')
    cursor = conn.cursor()
    
    # Criar tabela
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    ''')
    
    # Salvar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

# Função para inserir um novo usuário
def inserir_usuario(nome, idade):
    conn = sqlite3.connect('meu_banco_de_dados.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO usuarios (nome, idade)
    VALUES (?, ?)
    ''', (nome, idade))
    
    conn.commit()
    conn.close()

# Função para consultar todos os usuários
def consultar_usuarios():
    conn = sqlite3.connect('meu_banco_de_dados.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM usuarios')
    resultados = cursor.fetchall()
    
    conn.close()
    return resultados

# Função principal
def main():
    criar_tabela()
    
    # Inserir alguns dados
    inserir_usuario('Alice', 30)
    inserir_usuario('Bob', 25)
    
    # Consultar e exibir os dados
    usuarios = consultar_usuarios()
    print("Dados na tabela 'usuarios':")
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    main()
