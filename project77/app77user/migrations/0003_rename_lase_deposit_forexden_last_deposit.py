# Generated by Django 4.0.6 on 2022-08-29 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app77user', '0002_forexden'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forexden',
            old_name='Lase_Deposit',
            new_name='Last_Deposit',
        ),
    ]
