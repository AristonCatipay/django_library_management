# Generated by Django 4.2.7 on 2023-11-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0004_rename_authorlist_author_list_author_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='file',
            field=models.FileField(default=1, upload_to='thesis_files'),
            preserve_default=False,
        ),
    ]