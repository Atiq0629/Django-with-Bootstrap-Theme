# Generated by Django 3.2.5 on 2021-08-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
    ]
