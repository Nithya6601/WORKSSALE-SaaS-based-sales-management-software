# Generated by Django 4.0.1 on 2022-02-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0031_alter_admin_add_customer_table_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_add_customer_table',
            name='logger_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
