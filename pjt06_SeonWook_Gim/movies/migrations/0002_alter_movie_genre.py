# Generated by Django 4.2.5 on 2023-10-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('CM', 'Comedy'), ('FN', 'Fantansy'), ('RM', 'Romanace')], max_length=100),
        ),
    ]
