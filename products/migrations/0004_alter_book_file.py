# Generated by Django 4.2.2 on 2023-07-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_category_book_category_alter_author_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='file'),
        ),
    ]