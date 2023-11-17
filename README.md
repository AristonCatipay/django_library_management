![Librify](/readme_images/librify.png)
# Librify - a Library Management System

Librify is a Django library management system that have 3 different user types. Students, teachers and the admin. This library management system is design to be used in universities and is designed to store different books from different courses. 

## Run Locally

To use this application you have to clone this repository using git bash.

### Clone the repository
- Open the directory you want this application to be cloned. 
- Open git bash.

```bash
git clone https://github.com/AristonCatipay/django_library_management.git
```

### Install Dependencies

Activate virtual environment
```bash
pipenv shell
```

Install Django
```bash
pipenv install django
```

Install Pillow
```bash
pipenv install pillow
```

### If you want to use MySQL for your database. (Optional)
Install MySQL Client
```bash
pipenv install mysqlclient
```

Create a database named 'django_library_management' 
using your RDMS of choice (in this case using XAMPP Server).

![Create_a_database](/readme_images/xampp_create_database.png)

Edit your database configuration in the settings.py.
![Database_Configuration](/readme_images/change_database_settings.png)

Migrate
```bash
python manage.py migrate
```

### If you want to use PostgreSQL for your database. (Optional)
Install psycopg2
```bash
pipenv install psycopg2
```

Create a database named 'django_library_management' 
using your RDMS of choice.

![Create_a_database](/readme_images/postgre_create_database.png)

Edit your database configuration in the settings.py.
![Database_Configuration](/readme_images/postgre_change_database_settings.png)

Migrate
```bash
python manage.py migrate
```

### After you migrate to your database.

Start the server
```bash
python manage.py runserver
```

Create a super user.
```bash
python manage.py createsuperuser
```

Go to the admin page and login using the super user.

![Admin_Login](/readme_images/admin_login.png)

Create a new course named 'Not Specified' and abbreviation of 'NS'.

![Add_default_course](/readme_images/add_course_not_specified.png)

You can now start using the app normally.


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)