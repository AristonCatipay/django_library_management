# Generated by Django 4.2.6 on 2023-11-03 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_profile_student_contact_no_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0003_remove_reviewed_item_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewed_item',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='reviewed_item',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]