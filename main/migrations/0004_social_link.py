# Generated by Django 4.2.7 on 2023-11-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_achiever'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=200)),
                ('youtube', models.CharField(max_length=200)),
                ('Instagram', models.CharField(max_length=200)),
                ('Snapchat', models.CharField(max_length=200)),
                ('Twitter', models.CharField(max_length=200)),
                ('Pinterest', models.CharField(max_length=200)),
                ('Reddit', models.CharField(max_length=200)),
                ('LinkedIn', models.CharField(max_length=200)),
                ('Threads', models.CharField(max_length=200)),
            ],
        ),
    ]