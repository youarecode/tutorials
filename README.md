# tutorials
just a repository to try stuff

# Here there are some developer scripts and instructions
This Instructions are given by:

- [tutorial w3school](https://www.w3schools.com/django/)
  
## Setting up virtual environment
This creates a virtual environment with a python copy isolated from anything you do with your personal computer.

```python3 -m venv .venv```

The following folders have been created
- .venv
  - Include
  - Lib
  - Scripts
  - pyvenv.cfg

Now you have to activate the environment
```source .venv/bin/activate```
```deactivate```

Getting your requirements files.
```pip freeze > requirements.txt```
```pip install -r requirements.txt```


Note. You must activate the environment every time you open the command prompt on your project.

## Setting up Django
With the virtual environment activated, it's time to install the django framework.

```(my_env)... $ python -m pip install Django```

### Creating a Django Project
For the first time this command creates the scheme for this web.
```django-admin startproject portfolio_web```

This creates:
- \_\_init\_\_.py | This one says to python to search into the folder.
- settings.py | It stores all django configurations
    - Installed apps -> admin | auth | contenttypes | sessions | messages | static files
    - It uses SQLite3 by default
- url.py | here you store all urls paths for your web. (like an index for a book)
- wsgi.py | relative to the webserver you are going to use

#### Running the server
With this command you will have the server running at: http://127.0.0.1:8000/

```python manage.py runserver```


#### Migrate your project
This command start the database.
- it creates a sqlite3 database called `db.sqlite3` 
- This can be explored with an sqlite3 vscode extension

```python manage.py migrate```


#### Linking your app
Create a file in the same directory as your urls, called 'view.py'
- Here you dispatch your request to its respective response.


#### Define your templates
Templates are HTML files dedicated to format your frontend with changes from the backend.
- Include in your setting files, the directory for your templates



#### Creating your web app
This command initialize common files used for your app.
- My app was called 'webapp' so django has created a folder like that

```python manage.py startapp webapp```

This creates the following folders.
- 'views.py' | Here you store functions that takes http requests and returns http response
- 'models.py' | Here you store all database models and fields.


##### Defining your database model
After filling your 'models.py' file go to your settings file and include your webapp into the installed apps

1. include your webapp
```
INSTALLED_APPS = [..., 'webapp']
```

2. check for correctness
```python manage.py check webapp```

3. Build database tables from your models
```python manage.py makemigrations```

4. Previsualize those SQL commands that are going to build up your database
- the migration number is used
```python manage.py sqlmigrate webapp 0001```

5. Update your database with those SQL commands
```python manage.py migrate```

6. add some data from shell to test it out
```python manage.py shell
>>> from webapp.models import Article
art = Article(name='table',  category='decorative', price=90) #sql insert
art.save()
art_2 = Article.objects.create(name='drill', category='hardware store', price=65)
art.price = 95 #sql update
art.save()
art_3 = Article.objects.get(id=2)
art_3.delete() #sql delete
l = Article.objects.all() #sql select
l.query.__str__() #show the sql prompt

q=Article.objects.filter(category='decorative') #sql where
q=Article.objects.filter(category='decorative', price_gte=50) #where, and >=
q=Article.objects.filter(category='decorative', price_range=(10,150))
q=Article.objects.filter(price__gte=50).order_by('price') #order by price asc
q=Article.objects.filter(price__gte=50).order_by('-price') #order by price des
q=Article.objects.filter(name__icontains='table')#sql like
```

#### Using PosgreSQL
Install postgreSQL
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```
Install python library psycopg2
```
sudo apt install libpq-dev
(.env) ...$ pip install psycopg2```
Then verify with 'pip list'

---

1. try it on linux
```
sudo su - postgres
postgres@pc:~$ psql
```

2. New database
```CREATE DATABASE tutorial_db;```
3. List databases
```\l```


4. Define a password for your default user
```\password postgres
123456
```
4. Or create a new user [optional]
```
postgres@pc:~# create user my_name with password '123456';
postgres@pc:~# alter user my_name with superuser;
postgres@pc:~# CREATE DATABASE tutorial_db owner my_name;
```



5. Edit 'settings.py' file
```DATABASES = {
  ENGINE = django.db.backends.postgresql_psycopg2,
  NAME = 'tutorial_db',
  USER  = 'postgres',
  PASSWORD = '',
  HOST = 'localhost',
  PORT='',
}
```
6. Migrate the database
```python manage.py migrage```

7. Connect to database
```\connect tutorial_db;```
8. Show all tables
```\dt```

Exit pyql
```exit```


#### Create an administration site
By default the url is 'admin/'
- the administration site is useful for manage the model database. 

First you need to create the superuser
```python manage.py createsuperuser```

Remeber those database tables django created by default?
- in auth_users, is stored the users information.

If you want to edit your model's data, you can do it registering them in the 
- 'admin.py' | where you register your datamodels so the administrator can edit them
- if you want the headers of the data looks different, just edit the verbose_name for that variable name in that model.


#### Send Mail


Go to your google's account (search 'google app passwords')
- Security -> activate 2FA 
- Go to 2FA -> bottom and create your app password

```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' #Remember to configure your email account
EMAIL_USE_TLS = True #Security Protocol
EMAIL_PORT = 587 #for tls
EMAIL_HOST_USER = 'host@gmail.com'
EMAIL_HOST_PASSWORD = 'token_generated_by_googles_account' #Go to account, create access key
```

After configuring your settings.py file you are allowed to Send your email.
```
from django.core.mail import send_mail
send_mail('Subject', 'message', 'host_email@gmail.com', ['tgt_1@gmail.com','tgt_2@gmail.com'],fail_silently=False)
```
#### Security issues
So far we reallized there are many passwords store in the settings.py file 
which are publicly seen by everyone if the repository is public.

1. Unsecure way: 
- if a malicius guy knows the user and password, can have full access to your google's account
2. Save password in environment
- same unsecurity but at least you are not publishing it at github
3. Don't use your account's password, use a token.
- Tokens have certain permission contrains (i.e. forbidden change password)
- They can be nuled if some suspicious activity has been found
4. Use cloud secret systems to store those passwords instead of using your own environment.


Create your .env file in the same dir as your settings, then update settings.py 
```
pip install django-environ
----
import environ

env=environ.Env()
environ.Env.read_env() #choose where to read the env

#Now update your fields
DEBUG = env.bool('DEBUG', default=False)
```
#### OAuth
How to authenticate an user to their personal account
```
pip install django-allauth
```
Then follow the allauth instructions from  
- https://docs.allauth.org/en/latest/installation/quickstart.html
- also add the following line at 'settings.py'
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

```
Then configure your OAuth
- https://docs.allauth.org/en/latest/account/configuration.html
```
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #So you are certain that mail is valid
```

Other tools
- INLINE CSS #Use css via smtp
- Naomi #see template for mails in html


#### Templates
Google 'template web responsive'
- Templates that automatically adjusts to your screen (mobile, desktop)