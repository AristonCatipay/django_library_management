# Generated by Django 4.2.6 on 2023-10-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='student_contact_no',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_number',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]