# Generated by Django 3.2.7 on 2021-09-28 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locked_models', '0005_alter_editingnow_is_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editingnow',
            name='is_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]