# Generated by Django 5.0 on 2023-12-17 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Donor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.CharField(max_length=50)),
                ('street', models.CharField(default=' ', max_length=50)),
                ('barangay', models.CharField(default=' ', max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('UserID', models.BigAutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(default='', max_length=30, unique=True)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('EmailAddress', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=128)),
                ('Needs', models.CharField(choices=[('food', 'Food'), ('clothing', 'Clothing'), ('shelter', 'Shelter'), ('education', 'Education'), ('medical', 'Medical'), ('utilities', 'Utilities'), ('transportation', 'Transportation'), ('employment', 'Employment'), ('other', 'Other')], default='food', max_length=50)),
                ('UserType', models.CharField(choices=[('donor', 'Donor'), ('beneficiary', 'Beneficiary'), ('admin', 'Admin')], default='beneficiary', max_length=12)),
                ('Org', models.CharField(default='None', max_length=50)),
                ('Address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Beneficiary.address')),
                ('AmountTrackerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Donor.amount_tracker')),
                ('GoodsTrackerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Donor.goods_tracker')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
