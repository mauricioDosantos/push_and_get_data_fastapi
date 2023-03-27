## Projeto CRUD de cliente
Este projeto pode ser executado com o comando:

Configuração de ambiente:

Criar ambiente virtual:

> virtualenv -p 3 venv

Instalar dependências:

> pip install  -r requirements.txt

Colocar o servidor no ar:

> uvicorn main.app:app --reload

Abaixo segue uma collection do postman para executar o código:

> https://api.postman.com/collections/24607024-b8837e37-285f-4eb6-98b7-fa3a112c8d5b?access_key=PMAT-01GWGQF7JVPK2DXA3FG4TKT7WJ 

Também pode ser testado pelo comando curl

Exemplo:

> curl 'http://127.0.0.1:8000/clients/'
