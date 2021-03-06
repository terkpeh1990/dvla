# Generated by Django 3.2.6 on 2021-09-06 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20210906_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pv',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2000)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], max_length=15)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pv_details',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2000)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.pv')),
            ],
        ),
    ]
