# TABLEU PROMOTION EXTENSION BACKEND
El desarrolo de esta api es unicamente para ofrecer un vista, para poder almacenar la promocion generada en conjuntos con sus recomendaciones. A cada promción se le genera un ID unico
## Requirements

- [Python >= 3.6](https://www.python.org/)
- [Pipenv](https://github.com/pypa/pipenv)
- [PostgreSQL](https://www.postgresql.org/)

## Development

1. Clone repository: `git clone https://github.com/Joaquinecc/api-bristol.git`
2. Install dependencies: `pipenv install`
3. Create a file called `secrets.json` in root directory
4. Insert the following lines into the file:

   ```
   {
    "allowed_hosts": ["localhost", "127.0.0.1", <ANY_OTHER_HOST>],
    "db_name": "<DB_NAME>",
    "schemas": "<SCHEMA_NAME>",
    "secret_key": "<SECRET_KEY>",
    "db_user": "<POSTGRESQL_DB_USER>",
    "db_password": "<POSTGRESQL_DB_PASSWORD>",
    "db_host": "<POSTGRESQL_DB_HOST>",
    "db_port": "<POSTGRESQL_DB_PORT>",
    "debug": "<DEBUG_MODE>"

   }
   ```

5. Activate virtualenv: `pipenv shell`
6. Run migrations: `python manage.py migrate`
7. Create SuperUser: `python manage.py createsuperuser`
8. Run Development Server: `python manage.py runserver`
9. Run as https service `python manage.py runserver_plus --cert-file cert.pem --key-file key.pem 0.0.0.0:8000`
