# Generated by Django 4.2.4 on 2023-08-05 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
