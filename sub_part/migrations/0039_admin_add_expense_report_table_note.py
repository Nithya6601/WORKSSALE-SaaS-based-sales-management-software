# Generated by Django 4.0.1 on 2022-02-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0038_admin_add_expense_report_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_add_expense_report_table',
            name='note',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
