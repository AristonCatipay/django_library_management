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

### Install Dependencies

Install Pipenv

```bash
pip install pipenv
```

Activate Virtual Environment

```bash
pipenv shell
```

Make sure you have `Python 3.11`
Go to [Python 11](https://www.python.org/downloads/release/python-3119/)
If you have multiple installation of python. Choose the python 11.

```bash
pipenv --python path\to\python.exe
```

Install Dependencies

```bash
pipenv install
```

Migrate

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

### Update dependencies

```bash
pipenv update
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
