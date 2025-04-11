
### Setup

* `pip install -r requirements.txt`
* `env\Scripts\activate`
* `python manage.py runserver`


### Templates

* Create a template folder and add your htmls
* Go to main > settings and add the templates folder
```TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
```
* Then go to chatapp > views.py and add the routes