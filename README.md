Commands used :

To activate virtual env:
source .venv/bin/activate

To deactivate:
deactivate

To create django app:
first install pip
then to uses pip ->
python3 -m pip (command)

To run:
python3 manage.py runserver       

To create app:
python3 manage.py startapp appName     

In browser use SHIFT+RELOAD to refresh changes

After creating models, we have to make migrattions:
python3 manage.py makemigrations

To migrate:
python3 manage.py migrate

To enter into interactive shell:
python3 manage.py shell

Then:
from appname.models import classname
eg: from posts.model import Post
p = Post()
p.title = 'Something'
p.save() to enter it into database
exit() to exit out of the shell

override __str__ method to tell what to be shown when Post.objects.all() is called

To create Superuser for Django admin:
python3 manage.py createsuperuser

vishalkumar | vishal12345

