# Generated by Django 4.2.4 on 2023-08-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_control', '0005_alter_columnmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainmodel',
            name='plots',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
