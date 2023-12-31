# Generated by Django 4.2.7 on 2023-11-10 04:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('Sale', models.IntegerField()),
                ('Quote', models.CharField(max_length=250, null=True)),
                ('Discount_deal', models.CharField(choices=[('Hot Deals', 'Hot Deals'), ('New Arraivels', 'New Arraivels')], max_length=100)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '3. Banner',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_Name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image')),
            ],
            options={
                'verbose_name_plural': '2. Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('category_name', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': '5. Category',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '11. Colors',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '7. Section',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '8. Tag',
            },
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name_plural': '6. Sub_Category',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('Sale', models.IntegerField()),
                ('Discount_deal', models.CharField(choices=[('Hot Deals', 'Hot Deals'), ('New Arraivels', 'New Arraivels')], max_length=100)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=250, null=True)),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
            ],
            options={
                'verbose_name_plural': '1. Slider',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('product_name', models.CharField(max_length=250, null=True)),
                ('total_quantity', models.IntegerField()),
                ('total_availability', models.IntegerField()),
                ('sort_description', ckeditor.fields.RichTextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('model_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=500, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sub_category')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.color')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.section')),
                ('tags', models.ManyToManyField(to='product.tag')),
            ],
            options={
                'db_table': 'app_Product',
            },
        ),
        migrations.CreateModel(
            name='More_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_image', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=250, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name_plural': '9. Image',
            },
        ),
        migrations.CreateModel(
            name='Additional_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciation', models.CharField(max_length=250, null=True)),
                ('details', models.CharField(max_length=250, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name_plural': '10. Additional information',
            },
        ),
    ]
