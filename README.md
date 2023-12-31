![Librify](/readme_images/librify.png)
# Librify - Simplifying Library Management with Django

Librify is a Django-based library management system that enables students to efficiently search and filter through the library's collection of books and theses and allows them to borrow books and view theses files. It also allows librarians and staff to facilitate the smooth handling of book borrowing, return processes, and overdue notifications while managing the catalog of books and theses. You can use the built-in front end using Django templates or interact with the system via API.

### Features
- Comprehensive Search and Filter: Students can effortlessly search and filter through the library's diverse collection of books and theses, ensuring easy access to relevant resources.

- Borrowing and Thesis Viewing: Enables students to borrow books and access thesis files, promoting a smoother learning experience.

For library staff and administrators, Librify offers:

- Efficient Borrowing Management: Streamlines book borrowing, return processes, and sends overdue notifications, ensuring an organized and punctual system.

- Catalog Management: Empowers librarians to manage the catalog of books and theses efficiently, ensuring an updated and organized repository.

Librify aims to create a harmonious and efficient environment for students and staff, simplifying library operations and enhancing accessibility to valuable educational resources.

## Run Locally

To use this application you have to clone this repository using git bash.

### Clone the repository
- Open the directory you want this application to be cloned. 
- Open git bash.

```bash
git clone https://github.com/AristonCatipay/django_library_management.git
```

### Install Dependencies using `requirements.txt`
Install project dependencies
```bash
pip install -r requirements
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

Install Django REST Framework
```bash
pipenv install djangorestframework
```

Install Pillow
```bash
pipenv install pillow
```

Install Tailwind
```bash
pipenv install django-tailwind
```

Install Django Tailwind Reload
```bash
pipenv install django-tailwind[reload]
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

![Create_a_database](/readme_images/postgre_create_database.PNG)

Edit your database configuration in the settings.py.
![Database_Configuration](/readme_images/postgre_change_database_settings.png)

Migrate
```bash
python manage.py migrate
```

Start the server
```bash
python manage.py runserver
```

### Contact
For any inquiries or feedback, feel free to contact the project maintainers:

- Ariston Catipay - aristoncatipay123@gmail.com


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)