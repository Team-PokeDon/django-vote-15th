# Generated by Django 3.0.8 on 2022-05-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_add_team_column_to_MyUser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='team',
        ),
        migrations.AddField(
            model_name='candidate',
            name='team',
            field=models.CharField(default='', max_length=15),
        ),
    ]
