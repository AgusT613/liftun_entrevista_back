# Generated by Django 5.0 on 2023-12-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('action_start', models.DateField()),
                ('action_end', models.DateField(blank=True, null=True)),
                ('has_person_in_charge', models.BooleanField(default=False)),
                ('has_goals', models.BooleanField(default=False)),
                ('needs_carbon_footprint_calculation', models.BooleanField(default=False)),
                ('is_legal_duty', models.BooleanField(default=False)),
                ('action_type', models.CharField(choices=[('betterWorld', 'Better World'), ('betterPlace', 'Better Place'), ('betterCompany', 'Better Company'), ('betterProfit', 'Better Profit')], max_length=100)),
            ],
        ),
    ]
