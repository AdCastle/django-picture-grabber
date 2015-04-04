# django-picture-grabber
Instagram Django/Python tag grabber

# Requirements

You will need to install the Python - Instagram API - https://github.com/Instagram/python-instagram

You will also need to set up an Instagram OAuth account - https://instagram.com/developer/

# To run

Add your Instagram OAuth ID into the required location within the view.py file

python manage.py runserver

The page will refresh every 10000 ms

# Parameters

Grab all images with given tag

http://localhost:8000/instagram/?tag={TAG}

Display only a given amount of images

http://localhost:8000/instagram/?tag={TAG}&count={COUNT}

