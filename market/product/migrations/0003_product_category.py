# Generated by Django 4.2.6 on 2023-10-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_img_product_image_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vegetables', 'vegetables'), ('fruits', 'fruits'), ('meat', 'meat')], default='vegetables', max_length=25),
        ),
    ]
