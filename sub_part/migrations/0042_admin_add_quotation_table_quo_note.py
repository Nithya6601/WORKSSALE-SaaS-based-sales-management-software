# Generated by Django 4.0.1 on 2022-02-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0041_admin_add_quotation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_add_quotation_table',
            name='quo_note',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
