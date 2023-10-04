# AML-Application-205
python
Install virtualenv (if not already installed):

Before creating a virtual environment, you need to have virtualenv installed. If you are using Python 3.3 or newer, venv comes bundled with Python, so you can skip this step. Otherwise, you can install virtualenv using pip:
Copy code:
pip install virtualenv

Create a new virtual environment
Navigate to the root directory of your Django project in the terminal (or command prompt) and create a new virtual environment using virtualenv or venv (Python 3.3+):
For virtualenv copy code:
python -m venv venv
This will create a new folder named venv (you can use a different name if you prefer) containing the virtual environment.

Activate the virtual environment:
To activate the virtual environment, run the appropriate command based on your operating system:
For Windows copy code:
.\venv\bin\Activate.ps1 

Install dependencies
The initial dependencies can be installed from the  requirements.txt file.
Copy code:
pip install -r requirements.txt

Sometimes the Django module doesn't install properly. If so, run: pip install Django

Update the database models before creating a superuser:
cd aml_application
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

### Installing postgreSQL database
If pgAdmin is installed you should have 'SQL Shell (psql)' installed on your system as well. Run this program and enter the details to login to the postgres instance.
This should be by default:\
Server - 'localhost'\
Database - 'postgres'\
Port - '5432'\
Username - 'postgres'

Enter your password then run the following SQL command 
```SQL
CREATE DATABASE aml_application
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
```
The postgress password will need to be changed to 'Adminadmin123' using `\password postgres` in the SQL Shell

Ensure you run migrate and createsuperuser commands again on the new database

