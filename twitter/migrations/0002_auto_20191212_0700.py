# Generated by Django 3.0 on 2019-12-12 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='content',
            new_name='text',
        ),
    ]