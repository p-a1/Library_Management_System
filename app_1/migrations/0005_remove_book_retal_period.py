# Generated by Django 5.0.6 on 2024-08-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_alter_book_retal_period_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='retal_period',
        ),
    ]
