# Generated by Django 4.0.1 on 2022-02-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0035_admin_add_return_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_add_stock_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('logger_id', models.CharField(max_length=100)),
            ],
        ),
    ]
