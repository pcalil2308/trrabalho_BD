import streamlit as st
import pymysql
import pandas as pd
from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import serialization

# Função para obter a conexão com o banco de dados
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Juca2013!',
        db='padaria'
    )

# Função principal da aplicação
def main():
    st.title("Gestão de Padaria")

    menu = ["Clientes", "Funcionários", "Produtos", "Pedidos", "Relatórios"]
    choice = st.sidebar.selectbox("Menu", menu)

    conn = get_connection()
    cursor = conn.cursor()

    if choice == "Clientes":
        st.subheader("Clientes")
        if st.button("Mostrar todos os clientes"):
            query = "SELECT * FROM Cliente"
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        
        st.subheader("Adicionar Novo Cliente")
        with st.form(key='add_cliente'):
            nome = st.text_input("Nome do Cliente")
            telefone = st.text_input("Telefone")
            endereco = st.text_input("Endereço")
            submit_button = st.form_submit_button("Adicionar")

            if submit_button:
                query = "INSERT INTO Cliente (nome, telefone, endereco) VALUES (%s, %s, %s)"
                cursor.execute(query, (nome, telefone, endereco))
                conn.commit()
                st.success("Cliente adicionado com sucesso!")

    elif choice == "Funcionários":
        st.subheader("Funcionários")
        if st.button("Mostrar todos os funcionários"):
            query = "SELECT * FROM Funcionario"
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        
        st.subheader("Adicionar Novo Funcionário")
        with st.form(key='add_funcionario'):
            nome_funcionario = st.text_input("Nome do Funcionário")
            cargo = st.text_input("Cargo")
            submit_button = st.form_submit_button("Adicionar")

            if submit_button:
                query = "INSERT INTO Funcionario (nome_funcionario, cargo) VALUES (%s, %s)"
                cursor.execute(query, (nome_funcionario, cargo))
                conn.commit()
                st.success("Funcionário adicionado com sucesso!")

    elif choice == "Produtos":
        st.subheader("Produtos")
        if st.button("Mostrar todos os produtos"):
            query = "SELECT * FROM Produto"
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        
        st.subheader("Adicionar Novo Produto")
        with st.form(key='add_produto'):
            id_fornecedor = st.number_input("ID do Fornecedor", min_value=1)
            nome_produto = st.text_input("Nome do Produto")
            categoria = st.text_input("Categoria")
            estoque = st.number_input("Estoque", min_value=0)
            preco = st.number_input("Preço", min_value=0.0, format="%.2f")
            submit_button = st.form_submit_button("Adicionar")

            if submit_button:
                query = "INSERT INTO Produto (id_fornecedor, nome_produto, categoria, estoque, preco) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (id_fornecedor, nome_produto, categoria, estoque, preco))
                conn.commit()
                st.success("Produto adicionado com sucesso!")

    elif choice == "Pedidos":
        st.subheader("Pedidos")
        if st.button("Mostrar todos os pedidos"):
            query = """
                SELECT 
                    Pedido.id_pedido,
                    Cliente.nome AS cliente,
                    Funcionario.nome_funcionario AS funcionario,
                    Pedido.data_pedido,
                    Pedido.tipo_pedido,
                    Pedido.status_pedido
                FROM 
                    Pedido
                JOIN 
                    Cliente ON Pedido.id_cliente = Cliente.id_cliente
                JOIN 
                    Funcionario ON Pedido.id_funcionario = Funcionario.id_funcionario
            """
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)
        
        st.subheader("Adicionar Novo Pedido")
        with st.form(key='add_pedido'):
            id_cliente = st.number_input("ID do Cliente", min_value=1)
            id_funcionario = st.number_input("ID do Funcionário", min_value=1)
            data_pedido = st.date_input("Data do Pedido")
            tipo_pedido = st.text_input("Tipo de Pedido")
            status_pedido = st.text_input("Status do Pedido")
            submit_button = st.form_submit_button("Adicionar")

            if submit_button:
                query = "INSERT INTO Pedido (id_cliente, id_funcionario, data_pedido, tipo_pedido, status_pedido) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (id_cliente, id_funcionario, data_pedido, tipo_pedido, status_pedido))
                conn.commit()
                st.success("Pedido adicionado com sucesso!")

    elif choice == "Relatórios":
        st.subheader("Relatórios")
        if st.button("Relatório de Produtos por Fornecedor"):
            query = """
                SELECT 
                    Produto.id_produto,
                    Produto.nome_produto,
                    Produto.categoria,
                    Produto.estoque,
                    Produto.preco,
                    Fornecedor.nome_fornecedor AS fornecedor
                FROM 
                    Produto
                JOIN 
                    Fornecedor ON Produto.id_fornecedor = Fornecedor.id_fornecedor
            """
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)

        if st.button("Total de Produtos e Valor em Cada Pedido"):
            query = """
                SELECT 
                    Pedido.id_pedido,
                    Cliente.nome AS cliente,
                    SUM(Pedido_Produto.quantidade) AS total_itens,
                    SUM(Pedido_Produto.preco_unitario * Pedido_Produto.quantidade) AS valor_total
                FROM 
                    Pedido
                JOIN 
                    Pedido_Produto ON Pedido.id_pedido = Pedido_Produto.id_pedido
                JOIN 
                    Cliente ON Pedido.id_cliente = Cliente.id_cliente
                GROUP BY 
                    Pedido.id_pedido, Cliente.nome
            """
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(df)

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
