# Generated by Django 4.0.10 on 2023-08-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_wine_alcohol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='grape',
        ),
        migrations.AddField(
            model_name='wine',
            name='grape',
            field=models.ManyToManyField(to='database.grape'),
        ),
    ]
