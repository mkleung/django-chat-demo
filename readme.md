### Demo
[Live site](https://mpakleung.pythonanywhere.com/)

To do
- [x] Virtual Environment and setup
- [x] Routes
- [x] Templates
- [x] Database and Models
- [x] Rooms Crud Functionality
- [ ] Polls Crud Functionality
- [x] Search Rooms
- [x] Authentication
- [x] User Registration
- [x] Profile Management
- [x] ChatRoom
- [x] Activity Feed
- [x] Static Files (inside settings.py need to add configuration)
- [x] API (Django Rest Framework)
- [x] Cors Configuration
  

### Setup Virtual Environments
* Install python or check version `python --version`
* `pip install virtualenv`
* `mkdir project && cd project`
* `python -m venv env` (create environment file)
* `env\Scripts\activate` (activate environment file) or `source env/bin/activate` (mac)
* `pip install -r requirements.txt` (use this if you are installing from requirements file)

Install django and generate requirements file
* Note A django project can contain many apps
* `pip install django`
* `django-admin --version` (check version)
* `pip freeze > requirements.txt`

Create project
* `django-admin startproject demo` (creates project)
* `cd demo`
* `python manage.py startapp myapp` (creates app)

Link the App and start server
* Go to demo>settings.py and add "myapp" to the Installed_apps
* `python manage.py runserver`


### 1. Steps for adding route/template

* Create a urls.py inside myapp and add a path `path("", views.home, name="home")`
* Inside the main project: demo > urls.py, add the path `path('', include("myapp.urls")),`
* Create templates inside the myapp folder. (base.html and home.html)
* Inside myapp> views.py add

```
def home(request):
    return render(request, "home.html")
```

### 2. Setup Database with ORM

* Create a model inside the app>models.py
* Register the model with the admin.py  (this allows models to appear in admin panel)
* Make a migration. (a migration is an automated code that django will apply to db which allows you to change your models and update them)
* `python manage.py makemigrations`
* `python manage.py migrate`

### 3. Update Views

* create todos.html template inside app > templates 
* Create a view inside view.py inside app > views.py
* Create a url for the todos template inside app > urls.py 

### 4. View the admin panel

* `python manage.py createsuperuser`
* username: test, email: test@test.com, password: test
* Then go to [localhost](http://127.0.0.1:8000/admin)


### 5. Global Templates folder Setup**
* Create a template folder and add your htmls
* Go to main > settings and add the templates folder
```TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
    }
]
```
* Then go to chatapp > views.py and add the routes
* When creating a templates folder inside chatapp, it must be the same name



### 6. Django Rest Framework
* [Link](https://www.django-rest-framework.org/)
* `pip install djangorestframework`
* `pip install markdown`
* `pip install django-filter`
* main > settings.py
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### 7. Cors

* [Link](https://pypi.org/project/django-cors-headers/)
* `python -m pip install django-cors-headers`
* main > settings.py
```
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

* add the middleware in settings.py
```
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

* Setup allowed urls in settings.py

```
CORS_ALLOWED_ORIGINS = True
```

### Deployment to pythonanywhere

**Bash**
* https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
* Git clone your repo
* `$ mkvirtualenv --python=/usr/bin/python3.10 venv`
* `pip install -r requirements.txt`

**Create new app**
* Add a new app under python anywhere
* Select manual configuration
* Under virtualenv section add `venv`

**WSGI**
* Edit the wsgi.py file
```
import os
import sys
path = '/home/mpakleung/django-chat-demo'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
**Domain name**
Add this to settings.py
```
DEBUG = False

ALLOWED_HOSTS = ['mpakleung.pythonanywhere.com']
```

**Static Files**
* Add this to settings.py

```
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
* then run `python manage.py collectstatic`


**Under configuration**
Url: /static/
Directory: /home/myuser/django-chat-demo/static



Themes
* https://www.builtatlightspeed.com/theme/pixelcave-dark-web-app-dashboard
* https://preline.co/templates.html



Source

https://youtu.be/PtQiiknWUcI?si=0ROF5V-2pY0gO_iv&t=23400
