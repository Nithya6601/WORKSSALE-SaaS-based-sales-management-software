# Generated by Django 4.0.1 on 2022-02-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0042_admin_add_quotation_table_quo_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_add_expense_list_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
                ('exp_date', models.CharField(max_length=100)),
                ('exp_category', models.EmailField(max_length=254)),
                ('amount', models.CharField(max_length=100)),
                ('logger_id', models.CharField(max_length=100)),
            ],
        ),
    ]
