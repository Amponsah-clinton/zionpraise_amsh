# Generated by Django 5.1.7 on 2025-04-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_score_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
