# Generated by Django 4.2.6 on 2023-11-02 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
