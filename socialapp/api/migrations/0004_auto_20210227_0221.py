# Generated by Django 3.1.7 on 2021-02-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210227_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]