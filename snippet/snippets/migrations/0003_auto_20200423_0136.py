# Generated by Django 2.1 on 2020-04-23 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20200423_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='name',
            new_name='Name',
        ),
    ]
