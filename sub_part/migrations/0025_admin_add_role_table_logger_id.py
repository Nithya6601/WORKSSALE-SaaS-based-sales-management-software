# Generated by Django 4.0.1 on 2022-02-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0024_admin_add_role_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_add_role_table',
            name='logger_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
