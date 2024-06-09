# RAD API

Este é um projeto de API RAD (Rapid Application Development) desenvolvido em Flask.

## Participantes

- Yan Andrey Cruz de Paula, 202308397249

## Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- Docker

O ambiente de desenvolvimento do projeto foi configurado para operar exclusivamente com contêineres, aproveitando ao máximo a flexibilidade e portabilidade que o Docker oferece. No entanto, para aqueles que preferem ou necessitam de uma outra abordagem, também é possível executar a aplicação sem a dependência do Docker. Abaixo serão fornecidas instruções detalhadas para ambas as opções, garantindo que cada membro da equipe possa escolher o método que melhor se adapte às suas necessidades e preferências.

## Executando o Projeto

### Com Docker

1. Certifique-se de ter o Docker instalado em sua máquina.

2. Execute o docker-compose:

   ```sh
   docker-compose up --build
   ```

3. Acesse a API em [http://localhost:5000](http://localhost:5000).

### Sem Docker

1. Certifique-se de ter o Python 3.x instalado em sua máquina.

2. Certifique-se de ter o banco de dados Postgres instalado em sua máquina.

3. Ajuste a conexão com o banco de dados no arquivo `config.py`.

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Execute o aplicativo Flask:

   ```sh
   python app.py
   ```

6. Acesse a API em [http://localhost:5000](http://localhost:5000).

## Documentação da API
Você pode encontrar a documentação da API gerada automaticamente usando Swagger em:

[http://localhost:5000/swagger/](http://localhost:5000/swagger/)

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.