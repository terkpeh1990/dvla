# Generated by Django 3.2.6 on 2021-09-07 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0010_auto_20210907_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalloginrecords',
            old_name='is_account',
            new_name='is_manager',
        ),
        migrations.RenameField(
            model_name='historicalloginrecords',
            old_name='is_admin',
            new_name='is_standard',
        ),
        migrations.RenameField(
            model_name='loginrecords',
            old_name='is_account',
            new_name='is_manager',
        ),
        migrations.RenameField(
            model_name='loginrecords',
            old_name='is_admin',
            new_name='is_standard',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_bakery',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_bank',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_director',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_irishgreen',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_parent',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_partytree',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_principal',
        ),
        migrations.RemoveField(
            model_name='historicalloginrecords',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_bakery',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_bank',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_director',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_irishgreen',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_parent',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_partytree',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_principal',
        ),
        migrations.RemoveField(
            model_name='loginrecords',
            name='is_staff',
        ),
    ]
