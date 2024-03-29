# Generated by Django 4.2.6 on 2024-01-27 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matter', '0014_ip_matterimage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_matterimage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip_matterimage',
            name='docdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ip_matterimage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
