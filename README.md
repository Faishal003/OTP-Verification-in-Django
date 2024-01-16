# Email-OTP-Verification-in-Django
Email base send OTP and verify the user based on Django Framework.
# 💥Features Included💥
* Create an account.
* An otp send to your email.
* Verify User.
* Then login that user.
* Add try catch funtionality.
# Clone the Repository
After installing the prerequisite files just clone the project:<br>
```
https://github.com/Faishal003/Email-OTP-Verification-in-Django.git
```
# Installation
**Note :** Make sure you have Python version 3.10.x 👈<br>
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
Open up a browser and visit: <span style="color: blue;">http://127.0.0.1:8000/</span> , the you will see the Website💥❤️.<br>
All Set! 🤩🔥
# Note
In settings.py file, use your personal email and password. Make sure you have enabled two factor authentication and create an app password in your gmail account.
