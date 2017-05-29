# Chaos
## Mode-based random code responder app

### Windows Installation:

1. install python 3.*
2. install pip
3. From project's root, run:
    * `pip install virtualenvwrapper-win`
    * `mkvirtualenv chaos`
    * `workon chaos`
    * `python manage.py runserver`
    
For more installation info [click here](https://docs.djangoproject.com/en/1.11/howto/windows/)
### Usage:
1. To select mode, visit: http://localhost:8000/chaos/select
2. To get random code, visit: http://localhost:8000/chaos/response
3. To test application, run `python manage.py request`
4. To clear response pool, run `python manage.py clearpool`
5. To run unit tests, run `python manage.py test`
