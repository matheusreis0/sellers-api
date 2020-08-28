# sellers-api

## Database container
To create a container for postgres database, run:
```
docker run --name <container_name> -p 5432:5432 \
-e POSTGRES_PASSWORD=<some_password> \
-e POSTGRES_USER=<user_name> \
-e POSTGRES_DB=<database_name> \
-d postgres:12
```
To connect in django settings, add this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<user_name>',
        'PASSWORD': '<some_password>',
        'HOST': 'localhost',
        'PORT': ''
    }
}
```
