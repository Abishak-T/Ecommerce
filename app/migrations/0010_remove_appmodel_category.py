# Generated by Django 5.0.6 on 2024-07-25 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_appmodel_name_appmodel_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appmodel',
            name='category',
        ),
    ]
