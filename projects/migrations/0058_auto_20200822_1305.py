# Generated by Django 3.0.8 on 2020-08-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0057_auto_20200811_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='conditions',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
