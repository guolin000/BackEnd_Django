# Generated by Django 4.2.19 on 2025-03-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_content_encoding'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='年份'),
        ),
        migrations.AlterField(
            model_name='book',
            name='dynasty',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='朝代'),
        ),
    ]
