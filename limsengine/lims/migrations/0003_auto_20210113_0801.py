# Generated by Django 3.1.5 on 2021-01-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0002_auto_20210113_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='bb_from',
            field=models.IntegerField(blank=True, null=True, verbose_name='Б.Б с'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='bb_to',
            field=models.IntegerField(blank=True, null=True, verbose_name='Б.Б по'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='pallet_from',
            field=models.IntegerField(blank=True, null=True, verbose_name='паллеты с'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='pallet_to',
            field=models.IntegerField(blank=True, null=True, verbose_name='паллеты по'),
        ),
    ]
