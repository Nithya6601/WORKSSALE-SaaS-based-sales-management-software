# Generated by Django 4.0.1 on 2022-02-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_remove_admin_reg_table_conpass'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_customer_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.IntegerField()),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_city', models.CharField(max_length=100)),
                ('customer_state', models.CharField(max_length=100)),
                ('customer_country', models.CharField(max_length=100)),
                ('customer_zipcode', models.IntegerField()),
            ],
        ),
    ]
