# Generated by Django 3.2.8 on 2021-10-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='balanace',
        ),
        migrations.AddField(
            model_name='wallet',
            name='balance',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
