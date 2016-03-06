# SOS-backend 

REST API for SOS application. Done during VanHacks 2016 Hackathon. Deployed with Heroku.

Using Django, django-rest-framework.

##  APIs
host/user/
{GET} Retrieve list of users in database.
{POST} Create new user.

host/user/{user_uuid}
{GET} Retrieve detail view of {user_uuid} user.

host/sos/
{GET} Retrieve list of SOS requests in database.
{POST} Create new SOS request.

host/sos/{sos_uuid}
{GET} Retrieve detail view of {sos_uuid} SOS request.
{POST} Update current location of SOS request.

host/sos/{sos_uuid}/status
{GET} Retrieve status of {sos_uuid} SOS request.
{POST} Update status of {sos_uuid} SOS request.

(beta)
host/sos/{sos_uuid}/note
{GET} Retrieve notes from {sos_uuid} SOS request.
{POST} Add notes to {sos_uuid} SOS request.

host/sos/{sos_uuid}/image
{GET} Retrieve images from {sos_uuid} SOS request.
{POST} Add images to {sos_uuid} SOS request.


##  Installation

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:garpan12/vanhackprojackend.git
$ cd vanhackprojackend

$ pip install -r requirements.txt

$ createdb vanhackprojackend

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
