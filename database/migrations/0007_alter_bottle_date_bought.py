# Generated by Django 4.0.10 on 2023-09-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_wine_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='date_bought',
            field=models.DateField(null=True),
        ),
    ]
