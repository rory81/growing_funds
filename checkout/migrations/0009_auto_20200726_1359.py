# Generated by Django 3.0.8 on 2020-07-26 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0008_auto_20200726_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.UserProfile'),
        ),
    ]