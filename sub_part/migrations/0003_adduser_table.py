# Generated by Django 4.0.1 on 2022-01-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_reg_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='adduser_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user_role', models.CharField(max_length=100)),
                ('status_type', models.CharField(max_length=100)),
            ],
        ),
    ]
