# Generated by Django 4.0.3 on 2022-03-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='length',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='ptp',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='sold',
            field=models.BooleanField(default=False, null=True),
        ),
    ]