# Generated by Django 5.0.6 on 2024-07-25 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_submodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submodel',
            name='name',
        ),
    ]
