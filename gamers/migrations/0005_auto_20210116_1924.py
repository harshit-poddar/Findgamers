# Generated by Django 3.1.2 on 2021-01-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0004_auto_20210116_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='waiting_list',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
