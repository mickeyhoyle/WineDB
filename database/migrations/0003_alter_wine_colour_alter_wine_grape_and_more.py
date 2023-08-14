# Generated by Django 4.0.10 on 2023-08-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_wine_producer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='colour',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.colour'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='grape',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.grape'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='wine_type',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.winetype'),
        ),
    ]