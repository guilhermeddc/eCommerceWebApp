# Generated by Django 2.2.3 on 2019-07-22 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='feature',
            new_name='featured',
        ),
    ]
