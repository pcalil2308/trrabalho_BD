-- 6. Scripts em SQL DDL para criação do banco de dados e tabelas

CREATE DATABASE padaria; -- Cria o banco de dados chamado "padaria"
USE padaria; -- Define o banco "padaria" como o atual para execução dos próximos comandos

-- Criação da tabela Cliente
CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    telefone VARCHAR(15),
    endereco VARCHAR(150)
);

-- Criação da tabela Funcionario
CREATE TABLE Funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    nome_funcionario VARCHAR(100),
    cargo VARCHAR(50)
);

-- Criação da tabela Fornecedor
CREATE TABLE Fornecedor (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome_fornecedor VARCHAR(100),
    contato VARCHAR(15)
);

-- Criação da tabela Produto
CREATE TABLE Produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    id_fornecedor INT,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    estoque INT,
    preco DECIMAL(10, 2),
    FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id_fornecedor)
);

-- Criação da tabela Pedido
CREATE TABLE Pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    id_funcionario INT,
    data_pedido DATE,
    tipo_pedido VARCHAR(50),
    status_pedido VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

-- Criação da tabela Pedido_Produto (tabela intermediária para pedidos e produtos)
CREATE TABLE Pedido_Produto (
    id_pedido_produto INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT,
    id_produto INT,
    preco_unitario DECIMAL(10, 2),
    quantidade INT,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);

-- 7. Scripts em SQL DML para inserção de dados fictícios

-- Inserindo dados na tabela Cliente
INSERT INTO Cliente (nome, telefone, endereco) VALUES
('João Silva', '1111-1111', 'Rua A, 123'),
('Maria Souza', '2222-2222', 'Rua B, 456'),
('Carlos Lima', '3333-3333', 'Rua C, 789');

-- Inserindo dados na tabela Funcionario
INSERT INTO Funcionario (nome_funcionario, cargo) VALUES
('Ana Santos', 'Vendedor'),
('Pedro Oliveira', 'Gerente');

-- Inserindo dados na tabela Fornecedor
INSERT INTO Fornecedor (nome_fornecedor, contato) VALUES
('Fornecedor A', '9999-9999'),
('Fornecedor B', '8888-8888');

-- Inserindo dados na tabela Produto
INSERT INTO Produto (id_fornecedor, nome_produto, categoria, estoque, preco) VALUES
(1, 'Produto 1', 'Categoria X', 50, 10.00),
(1, 'Produto 2', 'Categoria Y', 30, 15.00),
(2, 'Produto 3', 'Categoria X', 20, 20.00);

-- Inserindo dados na tabela Pedido
INSERT INTO Pedido (id_cliente, id_funcionario, data_pedido, tipo_pedido, status_pedido) VALUES
(1, 1, '2024-11-01', 'Online', 'Processando'),
(2, 1, '2024-11-05', 'Loja', 'Concluído'),
(3, 2, '2024-11-10', 'Online', 'Cancelado');

-- Inserindo dados na tabela Pedido_Produto (relacionamento entre pedido e produto)
INSERT INTO Pedido_Produto (id_pedido, id_produto, preco_unitario, quantidade) VALUES
(1, 1, 10.00, 2),
(1, 2, 15.00, 1),
(2, 3, 20.00, 3),
(3, 1, 10.00, 5);

-- 8. Consultas SQL

-- a) Consultar todos os pedidos com informações sobre o cliente e o funcionário responsável
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
    Funcionario ON Pedido.id_funcionario = Funcionario.id_funcionario;

-- b) Relatório de Produtos com Informações do Fornecedor
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
    Fornecedor ON Produto.id_fornecedor = Fornecedor.id_fornecedor;

-- c) Total de Produtos e Valor em Cada Pedido
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
    Pedido.id_pedido, Cliente.nome;

-- d) Consulta de Estoque dos Produtos por Categoria
SELECT 
    categoria,
    SUM(estoque) AS total_estoque
FROM 
    Produto
GROUP BY 
    categoria;

-- e) View para Consultar Pedidos Pendentes
CREATE VIEW Pedidos_Pendentes AS
SELECT 
    Pedido.id_pedido,
    Cliente.nome AS cliente,
    Pedido.data_pedido,
    Pedido.tipo_pedido,
    Pedido.status_pedido
FROM 
    Pedido
JOIN 
    Cliente ON Pedido.id_cliente = Cliente.id_cliente
WHERE 
    Pedido.status_pedido = 'Processando';
