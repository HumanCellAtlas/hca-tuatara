# Generated by Django 2.1 on 2019-09-26 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hcat', '0004_auto_20190925_1727'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectState',
            new_name='ProjectStatus',
        ),
    ]
