# Generated by Django 4.2.6 on 2023-10-25 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('thesis', '0003_thesis_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthorList',
            new_name='Author_List',
        ),
        migrations.AddField(
            model_name='author',
            name='course',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='course.course'),
            preserve_default=False,
        ),
    ]
