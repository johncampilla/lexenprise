# Generated by Django 4.2.6 on 2024-03-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0083_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('RunDate', 'RunDate'), ('OA Mailing Date', 'OA Mailing Date'), ('Renewal Date', 'Renewal Date'), ('Publication Date', 'PublicationDate'), ('Document Receipt Date', 'Document Receipt Date'), ('IR Date', 'IR Date'), ('PCT Publication Date', 'PCT Publication Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('PCT Filing Date', 'PCT Filing Date'), ('Application Date', 'Application Date'), ('Registration Date', 'RegistrationDate'), ('Document Date', 'Document Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Priority Date', 'Priority Date')], max_length=30, null=True),
        ),
    ]
