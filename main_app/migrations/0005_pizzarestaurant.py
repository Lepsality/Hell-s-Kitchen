# Generated by Django 4.2 on 2023-05-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_size_rename_discription_menu_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaRestaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
