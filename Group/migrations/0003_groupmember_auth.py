# Generated by Django 3.0.3 on 2020-05-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_groupmember_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='auth',
            field=models.IntegerField(choices=[(0, 'President'), (1, 'Core-Members'), (2, 'Elder'), (3, 'Member')], default=3),
        ),
    ]