Commands used :

To activate virtual env:
source .venv/bin/activate

To deactivate:
deactivate

TO create django app:
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