Creating virtual Enviormnet
##########################

sudo pip3 install virtualenv
cd snippet
virtualenv newenv
source newenv/bin/activate

pip install django


Running Django server
#######################

python3 manage.py runserver


Accessing Webpage
##################

http://127.0.0.1:8000/admin/snippets/snippet/

username :vidya
passwd :hacker123

Setting New user
###############

python manage.py createsuperuser


Note :
--------------

Django Documentation is available under link : https://docs.djangoproject.com/en/3.0/intro/tutorial01/
