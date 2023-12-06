# Generated by Django 4.2.7 on 2023-12-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0002_rename_time_contact_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
