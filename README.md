# O QUE É?

Esse projeto é desenvolvido em Django com rest_framework para demonstrar como é um blog de notícias online.

# Passos Importantes

Obs: Primeiro de tudo crie uma venv e acesse-a se não tiver uma, para que o install fique apenas no ambiente virtual e não na própria máquina!

1 - Instalar os requerimentos do arquivo requirements.txt, para facilitar utilize o comando "pip install -r requirements.txt".
2 - Coloque as informações do seu banco de dados no arquivo .env.EXAMPLE e depois apague EXAMPLE, o docker compose já irá utilizar as variavéis de ambiente que estão lá e o settings.py do projeto também, então é só subir para o docker. (Já tem a configuração pronta, só mudar esses dados)
3 - faça as migrações do banco de dados e então migre.
4 - Agora o site poderá rodar com o banco PostgreSQL.

Alguns comandos serão necessários que sejam feitos pelo docker compose pois estão dentro do container.