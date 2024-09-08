Django Blog Project

Setting Up Virtual Environment
Before installing dependencies, it's a good practice to create a virtual environment for your project. Follow these steps:

Create a Virtual Environment:

Use the command python -m venv env to create a virtual environment in your project directory. This will create a folder named env in your project directory.

Activate the Virtual Environment:

On Windows, locate the env\Scripts\activate file to activate the virtual environment.
On macOS/Linux, locate the source env/bin/activate file to activate the virtual environment.


Prerequisites:
Before starting, ensure that you have Python installed on your system. Also, install the required database package for MySQL support:

pip install mysqlclient

Setting up the Project
1. Database Configuration:
You need to configure your database settings in the settings.py file. Find the DATABASES section and update it as per your MySQL configuration:

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'your_database_name', # Replace with your MySQL database name 'USER': 'your_mysql_username', # Replace with your MySQL username 'PASSWORD': 'your_mysql_password', # Replace with your MySQL password 'HOST': 'localhost', 'PORT': '3306', } }

2. Install Dependencies:
Run the following command to install all required packages from requirements.txt:

pip install -r requirements.txt

3. Migrate the Database:
After configuring the database, create the necessary tables in the database by running:

python manage.py makemigrations

python manage.py migrate

4. Create a Superuser:
To access the Django admin panel, create a superuser by running:

python manage.py createsuperuser

Follow the prompts to create your superuser account.

Project Features
1. CRUD Operations for Posts:
Authenticated users can create, edit, and delete posts.
Non-authenticated users can only view posts and leave comments.
Only the author of a post can edit or delete their own post.
2. Commenting System:
Non-authenticated users can leave comments on posts, but they cannot delete them.
Only the user who made the comment can delete their comment.
3. Search Functionality:
Users can search for posts using tags or keywords in the title or description.
4. User Authentication:
Implemented login, register, and logout functionalities to manage user access.
