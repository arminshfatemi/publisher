# Generated by Django 4.2.2 on 2023-06-28 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.IntegerField(blank=True)),
                ('birthday', models.DateTimeField(blank=True)),
                ('is_enable', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('is_enable', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_enable', models.BooleanField(default=True)),
                ('file', models.FileField(upload_to='files/Y%/m%/d%/', verbose_name='file')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ManyToManyField(blank=True, to='products.category')),
                ('author', models.ManyToManyField(to='products.author')),
            ],
        ),
    ]
