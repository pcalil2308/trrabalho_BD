# Padaria de Bairro - Modelagem de Banco de Dados

## 1. Descrição do Negócio

**Ramo de Atuação**  
Uma padaria de bairro que oferece uma variedade de pães, doces, bebidas e produtos artesanais. Atende tanto clientes locais quanto clientes que fazem encomendas para eventos especiais.

**Tipos de Serviços e Produtos Comercializados**
- **Produtos Diários:** Pães frescos (pão francês, integral, baguete), doces (bolos, tortas, salgados).
- **Encomendas Personalizadas:** Encomendas de bolos e tortas de aniversário, pão de festa e outros itens personalizados.
- **Bebidas:** Café, chá, sucos e refrigerantes.

## 2. Principais Atores

- **Cliente:** Compra produtos e pode solicitar encomendas personalizadas.
- **Funcionário:** Atendentes, caixas e padeiros que realizam atividades diárias.
- **Fornecedor:** Empresas ou produtores locais que fornecem insumos, como farinha, leite, chocolate e embalagens.
- **Gerente:** Responsável pela administração, controle de estoque, fluxo de caixa e gestão de funcionários.

## 3. Fluxo de Processos Cotidianos

- **Venda Direta ao Cliente:**  
  O cliente escolhe produtos disponíveis e realiza a compra. O pagamento é feito no ato, e o sistema atualiza o estoque dos produtos vendidos.

- **Encomendas:**  
  O cliente faz um pedido específico (ex: bolo personalizado), geralmente com antecedência. O pagamento pode ser antecipado ou parcelado, e a produção é agendada conforme a demanda e a disponibilidade de ingredientes.

- **Reposição de Estoque:**  
  Diariamente, o gerente verifica o estoque, solicita reposição aos fornecedores e agenda a produção de itens frescos.

## 4. Regras e Restrições do Negócio

- **Limite de Estoque:**  
  Certos produtos perecíveis, como pães e doces, têm produção limitada para evitar desperdício.

- **Pagamento Antecipado para Encomendas:**  
  Encomendas personalizadas exigem pagamento adiantado de ao menos 50% do valor.

- **Desconto para Clientes Frequentes:**  
  Clientes cadastrados com compras frequentes podem receber descontos em pedidos especiais ou promoções exclusivas.

- **Controle de Produção:**  
  A produção de itens personalizados depende da disponibilidade de ingredientes específicos e da capacidade da equipe.

## 5. Modelo Conceitual (MER)

### Cliente
- **id_cliente** (PK)
- **nome**
- **telefone**
- **endereco**

### Produto
- **id_produto** (PK)
- **nome_produto**
- **categoria** (ex.: pão, doce, bebida)
- **preco**
- **estoque**

### Pedido
- **id_pedido** (PK)
- **data_pedido**
- **tipo_pedido** (ex.: venda direta ou encomenda)
- **status_pedido** (ex.: pendente, concluído, cancelado)

### Fornecedor
- **id_fornecedor** (PK)
- **nome_fornecedor**
- **contato**

### Funcionário
- **id_funcionario** (PK)
- **nome_funcionario**
- **cargo**

---

Esse README.md fornece uma visão geral do modelo de negócios e da estrutura de banco de dados para a padaria. Ele inclui a descrição do negócio, os principais atores envolvidos, o fluxo de processos cotidianos, regras e restrições, e o modelo conceitual no padrão MER (Modelo Entidade-Relacionamento).
