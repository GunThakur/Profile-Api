# Generated by Django 4.2.9 on 2024-01-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('important', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='referral_code',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
