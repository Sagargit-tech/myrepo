# Generated by Django 3.1.3 on 2021-01-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customerid',
            field=models.IntegerField(),
        ),
    ]