# O QUE É?

Esse projeto é desenvolvido em Django com rest_framework e PostgreSQL para demonstrar como funciona um blog de notícias multi-organização com painel administrativo e dashboard de métricas.

# Passos Importantes

Obs: Caso rode algo fora do container, crie uma venv e acesse-a primeiro para que as instalações fiquem apenas no ambiente virtual e não na própria máquina. Porém, como o projeto roda inteiramente via container, todos os comandos do Django são feitos pelo Docker (ex: `docker compose exec django python manage.py ...`).

1 - Suba os containers com o Docker Compose (ele já instala automaticamente as dependências do arquivo `requirements.txt`, ou utilize `pip install -r requirements.txt` caso esteja na venv local).
2 - Coloque as informações do seu banco de dados no arquivo `.env.EXAMPLE` e depois renomeie para `.env` (apagando o `.EXAMPLE`). O Docker Compose e o `settings.py` já estão configurados para ler essas variáveis de ambiente automaticamente.
3 - Faça as migrações do banco de dados (`docker compose exec django python manage.py makemigrations` e `docker compose exec django python manage.py migrate`).
4 - Antes de acessar o sistema, crie seu usuário administrador pelo terminal do container com o comando: `docker compose exec django python manage.py createsuperuser`.
5 - Acesse `/admin/` com o usuário criado, cadastre uma Organização e crie um **Perfil** vinculado ao seu usuário definindo o papel como **Administrador** (`admin`) ou **Operador** (`operador`) — lembrando que o perfil de Operador possui funções reduzidas no site (não pode criar/editar posts, nem visualizar o gráfico mensal ou exportar CSV no dashboard). Sem esse perfil vinculado, o sistema bloqueará o acesso ao site e ao dashboard.

Alguns comandos serão necessários que sejam feitos pelo `docker compose` pois a aplicação e o banco PostgreSQL estão dentro dos containers.
