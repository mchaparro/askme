# Generated by Django 2.0.9 on 2018-12-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181212_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='long',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]