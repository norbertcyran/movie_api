# Generated by Django 2.2.3 on 2019-07-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rated',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='source',
            field=models.CharField(default='IMDb', max_length=20, verbose_name='Rating source'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='value',
            field=models.CharField(default='0', max_length=10, verbose_name='Rating value'),
            preserve_default=False,
        ),
    ]