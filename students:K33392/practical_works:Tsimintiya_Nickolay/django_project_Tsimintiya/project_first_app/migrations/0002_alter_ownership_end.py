# Generated by Django 4.2.6 on 2023-10-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_first_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ownership",
            name="end",
            field=models.DateField(blank=True, null=True),
        ),
    ]
