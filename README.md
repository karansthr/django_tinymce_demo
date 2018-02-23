This is a sample repository illustrating how to set up TinyCE editor with filebrowser in a Django site. For syntax highlighting, highlightjs is used.

Complete guide at - https://fosstack.com/how-to-set-up-tinymce-in-django-app/

# Installation guide

1) Clone repository ```git clone https://github.com/karansthr/django_tinymce_demo ```
2) cd (change directory) to repository.
3) Create a virtualenv ``` virtualenv -p python3 venv ```
4) Activate virtualenv ``` source venv/bin/activate  ```
5) Install required packages ``` pip3 install -r requirements.txt  ```
6) cd to ```blog ```
7) Run collectstatic command  ``` python3 manage.py collectstatic  ```
8) Run the server ``` python3 manage.py runserver  ```

If you want to access admin panel then go to localhost:[port]/admin and login with username = fosstack = fosstack
or you can create new user with ```python python3  manage.py createsuperuser ``
