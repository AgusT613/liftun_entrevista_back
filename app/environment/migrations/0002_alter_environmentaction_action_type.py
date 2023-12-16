# Generated by Django 5.0 on 2023-12-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentaction',
            name='action_type',
            field=models.CharField(choices=[('Better World', 'Better World'), ('Better Place', 'Better Place'), ('Better Company', 'Better Company'), ('Better Profit', 'Better Profit')], max_length=100),
        ),
    ]