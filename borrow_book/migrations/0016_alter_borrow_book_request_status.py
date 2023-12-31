# Generated by Django 4.2.7 on 2023-12-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0015_alter_borrow_book_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_book',
            name='request_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Request', 'Request'), ('Returned', 'Returned'), ('Borrowed', 'Borrowed'), ('Pending', 'Pending')], default='Request', max_length=15),
        ),
    ]
