# Generated by Django 4.2.4 on 2023-09-12 14:08

import application.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=application.models.getFileName)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=application.models.getFileName)),
                ('quantity', models.IntegerField()),
                ('originol_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-default,1-trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.catagory')),
            ],
        ),
    ]
