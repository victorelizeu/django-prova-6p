# O QUE É?

Esse projeto é desenvolvido em Django com rest_framework e PostgreSQL para demonstrar como funciona um blog de notícias multi-organização com painel administrativo e dashboard de métricas.

# Passos Importantes

Obs: Caso rode algo fora do container, crie uma venv e acesse-a primeiro para que as instalações fiquem apenas no ambiente virtual e não na própria máquina. Porém, como o projeto roda inteiramente via container, todos os comandos do Django são feitos pelo Docker (ex: `docker compose exec web python manage.py ...`).

1 - Suba os containers com o Docker Compose (ele já instala automaticamente as dependências do arquivo `requirements.txt`, ou utilize `pip install -r requirements.txt` caso esteja na venv local).
2 - Coloque as informações do seu banco de dados no arquivo `.env.EXAMPLE` e depois renomeie para `.env` (apagando o `.EXAMPLE`). O Docker Compose e o `settings.py` já estão configurados para ler essas variáveis de ambiente automaticamente.
3 - Faça as migrações do banco de dados (`makemigrations` e `migrate`) e crie um superusuário (`createsuperuser`) pelo container.
4 - Acesse `/admin/`, crie uma Organização e vincule um Perfil ao seu usuário (com papel `admin` ou `operador`) para liberar o acesso ao site e ao dashboard.

Alguns comandos serão necessários que sejam feitos pelo `docker compose` pois a aplicação e o banco PostgreSQL estão dentro dos containers.
