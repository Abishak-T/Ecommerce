# Generated by Django 5.0.6 on 2024-07-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_img', models.ImageField(blank=True, upload_to='')),
                ('name', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
    ]
