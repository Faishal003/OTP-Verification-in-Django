# Email-OTP-Verification-in-Django
![Static Badge](https://img.shields.io/badge/python-3.10-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3100%2F) ![Static Badge](https://img.shields.io/badge/django-5.0-orange)<br>
The email base sends OTP and verifies the user based on the Django Framework.
# 💥Features Included💥
* Create an account.
* An OTP is sent to your email.
* The verification link is valid for one minute.
* Verify User.
* Then log in to that user.
* Add try-catch functionality.
# Clone the Repository
After installing the prerequisite files just clone the project:<br>
```
https://github.com/Faishal003/Email-OTP-Verification-in-Django.git
```
# Installation
**Note:** Make sure you have Python version 3.10.x 👈<br>
Install a few prerequisite files before running the project 👀<br>
```
pip install -r requirements.txt 
```
# Create Superuser
Run command in terminal:
```
python manage.py createsuperuser
```
# Model Build
After creating `superuser`, run the following commands in the Terminal:
```
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
```
# Getting started to run the server
Run command in terminal:<br>
Execute: `python manage.py runserver`<br>
Open up a browser and visit: <span style="color: blue;">http://127.0.0.1:8000/</span> , then you will see the Website💥❤️.<br>
All Set! 🤩🔥
# Note
In the settings.py file, use your email and password. Make sure you have enabled two-factor authentication and create an app password in your Gmail account.
