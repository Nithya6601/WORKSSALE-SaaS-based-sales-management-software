# Generated by Django 4.0.1 on 2022-02-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0018_rename_add_brand_admin_addbrand_table_brand_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_addtax_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=100)),
                ('tax_percentage', models.CharField(max_length=100)),
                ('tax_dafault', models.CharField(max_length=100)),
            ],
        ),
    ]
