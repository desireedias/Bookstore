# 📚 Bookstore API

API REST para gerenciamento de produtos, categorias e pedidos, desenvolvida com Python, Django e Django REST Framework.

O projeto foi desenvolvido durante minha formação em Backend Python, com foco na construção de APIs, autenticação, paginação e testes automatizados.

## 🚀 Funcionalidades

- CRUD de produtos;
- CRUD de categorias;
- CRUD de pedidos;
- Autenticação por token;
- Controle de acesso a endpoints;
- Paginação de resultados;
- Ordenação de registros;
- Relacionamento entre produtos e categorias;
- Validação e serialização de dados;
- Testes automatizados de serializers e endpoints.

## 🛠️ Tecnologias

- Python
- Django
- Django REST Framework
- PostgreSQL
- Pytest
- Factory Boy

## 📂 Estrutura do projeto

```text
bookstore/
├── bookstore/       # Configurações principais do projeto
├── product/         # Produtos, categorias e regras relacionadas
├── order/           # Pedidos e regras relacionadas
├── tests/           # Testes automatizados
├── manage.py
└── README.md
