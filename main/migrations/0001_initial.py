# Generated by Django 4.2.7 on 2023-11-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('title', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('link', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Slider',
            },
        ),
    ]
