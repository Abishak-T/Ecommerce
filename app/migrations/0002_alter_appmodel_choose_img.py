# Generated by Django 5.0.6 on 2024-07-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='choose_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
