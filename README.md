# AgilStore - Gerenciamento de Produtos

## Descrição

A aplicação **AgilStore** é um sistema simples para o gerenciamento de inventário de uma loja de eletrônicos. Ela foi criada para otimizar o controle de estoque, facilitando operações como adicionar, listar, atualizar, excluir e buscar produtos. Os dados dos produtos são armazenados em um arquivo **JSON**, garantindo a persistência dos dados entre as execuções.

## Funcionalidades

- **Adicionar Produto**: Permite ao usuário adicionar um novo produto ao inventário.
- **Listar Produtos**: Exibe todos os produtos cadastrados com informações como ID, nome, categoria, quantidade em estoque e preço.
- **Atualizar Produto**: Permite atualizar as informações de um produto existente identificando-o pelo seu ID.
- **Excluir Produto**: Exclui um produto do inventário pelo ID após confirmação do usuário.
- **Buscar Produto**: Permite buscar um produto específico pelo seu ID ou nome.
- **Persistência de Dados**: Todos os dados dos produtos são salvos em um arquivo **JSON**.

## Requisitos

- Python 3.x
- Nenhuma dependência externa necessária.

## Como rodar a aplicação localmente

1. **Clonar o repositório**:
   
   Primeiramente, clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/Rutiele93/Gerenciamento-de-Produtos---Python.git

2. **Criar um ambiente virtual:**

   Navegue até o diretório do projeto e crie um ambiente virtual:
   ```bash
    python -m venv venv

3. **Ativo ou ambiente virtual:**   

   - No Windows , use o seguinte comando:
      ```bash
      .\venv\Scripts\activate
   
   - Sem MacOS/Linux , use:
       ```bash
      source venv/bin/activate

4. **Rodar a aplicação**
   
   Execute o arquivo principal para iniciar o aplicativo:
    ```bash
    python main.py

## Tecnologias Utiliza
- Python 3.x : Linguagem utilizada para o desenvolvimento da aplicação.
- JSON:  O formato JSON é utilizado para persistir os dados dos produtos no arquivo inventory.json. Ele permite salvar as informações de maneira estruturada e recuperá-las quando a aplicação for reiniciada.

## Funcionalidades Futuras (Opcionais)
- Filtragem de Produtos : Permite ao usuário filtrar os produtos por categoria, facilitando a busca por tipo de produto.
- Ordenação de Produtos : Adicione a opção de ordenar os produtos por nome, quantidade ou preço, permitindo que o usuário veja a lista de produtos de acordo com os critérios desejados.
