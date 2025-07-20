
🐦 CloneX – Clone do Twitter com Django

CloneX é um projeto de rede social inspirado no Twitter, desenvolvido como parte de um curso de Desenvolvimento Full Stack. A aplicação utiliza Django e Django REST Framework para fornecer uma API robusta com funcionalidades sociais modernas, como:

- Cadastro e login de usuários
- Criação, curtir e comentar tweets
- Seguir e deixar de seguir outros usuários
- Visualização de tweets da sua rede

------------------------------------------------------------

🚀 Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias e ferramentas:

- Python
- Django
- Django REST Framework (DRF)
- Poetry – Gerenciador de dependências e ambientes virtuais
- SQLite – Banco de dados leve para desenvolvimento
- Docker – Containerização e orquestração de serviços
- Pytest + Factory Boy – Testes automatizados e geração de dados de teste

------------------------------------------------------------

⚙️ Como Rodar o Projeto

Siga os passos abaixo para clonar e executar o CloneX localmente com Docker:

1. Clone o repositório:
   git clone https://github.com/lufehilario/CloneX.git

2. Acesse a pasta do projeto:
   cd CloneX

3. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias. Use o arquivo `env.dev` (caso exista) como referência.

4. Suba os containers com Docker Compose:
   docker-compose up -d --build

5. Aplique as migrações e colete os arquivos estáticos:
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --no-input

6. Acesse a aplicação no navegador:
   http://127.0.0.1:8000/

------------------------------------------------------------

📁 Estrutura do Projeto (resumo)

CloneX/
├── api/                # Aplicação principal (views, serializers, urls, models)
├── twitter/            # Configuração principal do projeto Django
├── tests/              # Testes automatizados
├── Dockerfile          # Configuração do container da aplicação
├── docker-compose.yml  # Orquestração dos containers
├── .env                # Variáveis de ambiente (não versionado)
├── pyproject.toml      # Dependências do projeto (Poetry)
└── README.md           # Este arquivo

------------------------------------------------------------

🙌 Contribuindo

Este projeto é parte de um estudo, mas sugestões e melhorias são bem-vindas! Fique à vontade para abrir issues ou enviar pull requests.

