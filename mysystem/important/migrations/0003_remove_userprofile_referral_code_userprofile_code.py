# Generated by Django 4.2.9 on 2024-01-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('important', '0002_alter_userprofile_referral_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='referral_code',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='code',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]