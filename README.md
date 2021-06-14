## Considerações iniciais

Esta aplicação é um sistema de controle de vagas e candidatos.

## Montar o app

1. Para executar o projeto é necessário clonar o repositório `git clone https://github.com/lacerdarenato/JobConvo.git` dentro do diretório em deseja instalá-lo.
2. Instalar as dependencias contidas no arquivo reuirements.txt através do comando `pip install -r requirements.txt`
3. Executar as migrações para montar o banco
   - `python manage.py makemigrations accounts`
   - `python manage migrate`
   - `python manage.py makemigrations candidato empresas vagas`
   - `python manage migrate`
        
4. Levantar o server através do comando `python manage.py runserver` 
5. Ele rodará através da URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/) onde o usuário interagirá com a aplicação.


## Considerações finais.

- Gostaria de agradecer a oportunidade de participar do processo seletivo, 
  sei que a aplicação ainda tem muito o que melhorar mas pretendo terminá-la posteriormente depois 
  que entender melhor como manipular a classe user este foi um dos pontos mais críticos na execução deste projeto.


## De qualquer forma e com qualquer resultado, gostaria de agradecer pela oportunidade. 
## Abraços e se cuidem!