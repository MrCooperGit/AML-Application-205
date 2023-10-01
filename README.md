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

