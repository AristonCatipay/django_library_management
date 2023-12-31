# Generated by Django 4.2.6 on 2023-10-27 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('borrow_book', '0005_alter_borrow_book_fine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_book',
            name='request_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Request', 'Request'), ('Borrowed', 'Borrowed')], default='Request', max_length=15),
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='staff_approve',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staff_approve_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='staff_borrow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staff_borrow_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='borrow_book',
            name='staff_return',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staff_return_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
