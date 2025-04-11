Source

https://youtu.be/PtQiiknWUcI?si=ncZpnYS4eTqFEh36&t=3892


### Setup

* `pip install -r requirements.txt`
* `env\Scripts\activate`
* `python manage.py runserver`


### Notes

Project Structure
* Main is the one containing settings and can have many apps (chatapp)
* Chatapp is a single individual app that contains templates.
* The templates folder outside the main and chatapp contains views that are used by all apps

Global Templates folder Setup
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
* When creating a templates folder inside chatapp, it must be the same name