# Generated by Django 4.0.6 on 2022-08-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app77user', '0004_rename_forexden_forexdenmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ForexDenModel',
        ),
        migrations.AddField(
            model_name='customuser',
            name='Balance',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Earned_Commission',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Earning',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Last_Deposit',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Pending_Withdrawal',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='Referals',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
