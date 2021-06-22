# Generated by Django 3.2.4 on 2021-06-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'actors3',
            },
        ),
        migrations.CreateModel(
            name='Movie3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('actors', models.ManyToManyField(to='movies.Actor3')),
            ],
            options={
                'db_table': 'movies3',
            },
        ),
    ]
