# Generated by Django 4.0.1 on 2022-01-30 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0004_adduser_table_logger_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='adduser_table',
            new_name='admin_adduser_table',
        ),
    ]
