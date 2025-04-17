Source

https://youtu.be/PtQiiknWUcI?si=DwA1y19SqNvXb9FD&t=14400

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
- [ ] Theme Installation
- [ ] Mobile Responsive
- [ ] Rest Framework
  
MVP
* Chat feature
* Chat rooms
* connect to language translate api


### Setup
* Download Django from [link](https://www.djangoproject.com/download/)
* `pip install virtualenv`
* `python3.13 -m venv env` (mac) or `python -m venv env` (windows)
* `source env/bin/activate` (mac) or `env\Scripts\activate` (windows)
* `pip install -r requirements.txt`
* `deactivate`

### Run the server
* `python manage.py runserver`


### Notes

**Project Structure**
* Main is the one containing settings and can have many apps (chatapp)
* Chatapp is a single individual app that contains templates.
* The templates folder outside the main and chatapp contains views that are used by all apps

**Global Templates folder Setup**
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

**Migrations**
* `python manage.py makemigrations`  (similar to git commit)
* `python manage.py migrate`    (similar to git push)
* `py manage.py shell`
* Superuser: admin, pass: test

To access the admin panel,
* `python manage.py createsuperuser`
* username: test
* To see the new model created, go to chatapp > admin.py
* Add this code 
`from .models import Room
admin.site.register(Room)`

