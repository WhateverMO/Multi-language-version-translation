# Multi language version translation

this project is a bookstore web application which can manage multi language version for translation.

## effect and structure

### frontend

this is the home page of our website.

![](pic/d2130c70f6177701f5afc04a7707c495.png)

### backend

this is how the backend structed.

![](pic/系统架构图.png)

### Database

this is how mysql database organized.

![](pic/img_1.png)

each book in sql is mapped from the root book in redis.

this is how redis database organized.

![](pic/img.png)

### transformer translate

this is the example of ai translate

![](pic/img_2.png)

## how to use

install pyenv and pipenv in your distribution first.

and then do following command to init python venv:

```bash
pyenv install 3.11.3
cd path/of/this/project
pyenv local 3.11.3
pipenv install
```

run backend:

```bash
# this command will background running
pipenv run python manage.py &
```

run frontend as dev:

```bash
cd web
npm run server
```

or you can use nginx to run the fronted:

```bash
# edit the nginx.conf to change the fronted path and server address
vim nginx.conf
nginx -c nginx.conf
```