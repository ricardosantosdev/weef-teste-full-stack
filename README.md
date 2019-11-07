# Weef Teste Full-Stack

## Installation for local test or development.

1. Clone this repository.

 ```
   git clone https://github.com/ricardosantosdev/weef-teste-full-stack.git
 ```

 2. Install the dependencies.

 ```
   pip install -r requirements.txt
 ```

 3. Create the database tables.

```
   $ python manage.py makemigrations
```

 4. Migrate data.

   ```
   $ python manage.py migrate
   ```

5. Finally, go work!

```
$ python manage.py runserver
```