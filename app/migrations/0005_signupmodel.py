# Generated by Django 5.0.6 on 2024-07-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_submodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signname', models.TextField(null=True)),
                ('signemail', models.EmailField(max_length=254, null=True)),
                ('signpass', models.TextField(null=True)),
                ('signconpass', models.TextField(null=True)),
            ],
        ),
    ]
