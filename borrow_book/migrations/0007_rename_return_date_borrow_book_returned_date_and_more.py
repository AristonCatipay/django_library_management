# Generated by Django 4.2.6 on 2023-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_book', '0006_alter_borrow_book_request_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow_book',
            old_name='return_date',
            new_name='returned_date',
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='request_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Returned', 'Returned'), ('Pending', 'Pending'), ('Borrowed', 'Borrowed'), ('Request', 'Request')], default='Request', max_length=15),
        ),
    ]
