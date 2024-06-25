# Projeto de Aplicação Web para a Papelaria Rabisco

## 💤 Introdução - 
Este projeto visa desenvolver uma aplicação web para a papelaria Rabisco, utilizando tecnologias modernas como React, Next.js e Flask. O objetivo é criar uma experiência de usuário dinâmica e eficiente.

## ✔ Componentes da Aplicação - 

### 1 - Interface Principal

 - Cabeçalho (Headerb): Inclui um campo de busca para pesquisar produtos.
   Utiliza o estado do React para gerenciar o termo de busca e realiza requisições à API.

 - Lista de Produtos (Card_List): Exibe os produtos da papelaria.

 - Cartão de Produto (Card_Prods): Mostra detalhes como imagem, nome, descrição, preço e quantidade em estoque.

### 2 - Gerenciamento de Funcionários

 - Componente Employees: Faz uma requisição à API para obter a lista de funcionários.
   
 - Cartão de Funcionário (Card_func): Exibe informações como avatar, nome, sobrenome e e-mail em um formato de cartão.

### 3 - Carrossel de Imagens
 - Carrossel (Carrossel): Permite a navegação entre diferentes slides de imagens, promovendo produtos ou serviços da papelaria.

## 🅱 Backend e API - 
1 - Estrutura do Backend
 - Desenvolvido em Flask, fornece uma API RESTful para gerenciar dados da papelaria.
   
 - Conecta-se a um banco de dados MySQL para operações de CRUD (Create, Read, Update, Delete) com produtos e funcionários.
   
2 - Funcionalidades da API
 - Inserção de Produtos: Adicionar novos produtos ao banco de dados.
   
 - Listagem de Produtos: Exibir todos os produtos disponíveis.
   
 - Atualização de Informações: Atualizar dados de produtos existentes.
   
 - Exclusão de Produtos: Remover produtos do banco de dados.

## 🔍 Busca de Produtos
 - Funcionalidade que permite aos usuários encontrar rapidamente os itens desejados.
   
 - Integração entre frontend e backend para garantir dados atualizados em tempo real.

## Conclusão
Este projeto combina tecnologias de frontend e backend para criar uma aplicação web completa. A estrutura modular facilita a manutenção e a escalabilidade, garantindo que a papelaria Rabisco possa crescer e se adaptar às necessidades futuras.
