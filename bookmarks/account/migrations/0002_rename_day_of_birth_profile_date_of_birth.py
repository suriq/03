# Generated by Django 5.1.6 on 2025-02-08 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='day_of_birth',
            new_name='date_of_birth',
        ),
    ]
