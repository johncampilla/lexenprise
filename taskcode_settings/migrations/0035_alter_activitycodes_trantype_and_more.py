# Generated by Django 4.2.6 on 2024-01-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0034_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('MAILSIN', 'MAILSIN'), ('BILLABLE', 'BILLABLE')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Months', 'In Months'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Document Receipt Date', 'Document Receipt Date'), ('Document Date', 'Document Date'), ('Priority Date', 'Priority Date'), ('OA Mailing Date', 'OA Mailing Date'), ('RunDate', 'RunDate'), ('Registration Date', 'RegistrationDate'), ('IR Date', 'IR Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Renewal Date', 'Renewal Date'), ('Publication Date', 'PublicationDate'), ('Application Date', 'Application Date'), ('IR Renewal Date', 'IR Renewal Date'), ('PCT Filing Date', 'PCT Filing Date')], max_length=30, null=True),
        ),
    ]
