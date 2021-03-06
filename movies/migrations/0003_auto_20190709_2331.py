# Generated by Django 2.2.3 on 2019-07-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190709_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rating',
            name='source',
            field=models.CharField(max_length=100, verbose_name='Rating source'),
        ),
    ]
