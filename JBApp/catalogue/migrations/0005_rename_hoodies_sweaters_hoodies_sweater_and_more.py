# Generated by Django 4.0.3 on 2022-08-11 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_exclusive_apparel_hoodies_sweaters_pants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hoodies_Sweaters',
            new_name='Hoodies_Sweater',
        ),
        migrations.RenameModel(
            old_name='Pants',
            new_name='Pant',
        ),
        migrations.RenameModel(
            old_name='Tees',
            new_name='Tee',
        ),
    ]