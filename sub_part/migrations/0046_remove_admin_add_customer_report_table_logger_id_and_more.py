# Generated by Django 4.0.1 on 2022-02-20 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0045_add_customer_report_table_add_customer_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_add_customer_report_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_customer_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_expense_list_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_expense_report_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_productlist_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_purchase_tax_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_quotation_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_return_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_role_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_sale_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_stock_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_add_vendor_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_addbrand_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_addcategory_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_addtax_table',
            name='logger_id',
        ),
        migrations.RemoveField(
            model_name='admin_adduser_table',
            name='logger_id',
        ),
    ]
