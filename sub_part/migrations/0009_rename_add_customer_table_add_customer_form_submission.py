# Generated by Django 4.0.1 on 2022-02-03 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0008_add_customer_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_customer_table',
            new_name='add_customer_form_submission',
        ),
    ]
