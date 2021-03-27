# Generated by Django 3.1.4 on 2021-03-25 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ManyToManyField(related_name='follower', to='api.Profile')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Following',
        ),
    ]
