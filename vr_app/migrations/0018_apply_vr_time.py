# Generated by Django 2.2.3 on 2019-08-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr_app', '0017_remove_apply_sms'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='vr_time',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
