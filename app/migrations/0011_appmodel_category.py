# Generated by Django 5.0.6 on 2024-07-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_appmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmodel',
            name='category',
            field=models.TextField(null=True),
        ),
    ]
