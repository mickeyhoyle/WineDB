# Generated by Django 4.0.10 on 2023-09-10 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_bottle_date_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
