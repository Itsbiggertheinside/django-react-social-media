# Generated by Django 3.1.4 on 2021-03-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
