# Generated by Django 4.2.6 on 2023-10-27 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('borrow_book', '0002_borrow_book_book_alter_borrow_book_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow_book',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='created_by_id', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='request_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Request', 'Request'), ('Borrowed', 'Borrowed'), ('Pending', 'Pending')], default='Request', max_length=15),
        ),
    ]
