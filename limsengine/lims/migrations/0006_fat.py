# Generated by Django 3.1.5 on 2021-01-13 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0005_auto_20210113_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blank_cup_mass', models.FloatField(blank=True, null=True, verbose_name='масса пустого стакана')),
                ('sample_mass', models.FloatField(blank=True, null=True, verbose_name='масса навески')),
                ('final_cup_mass', models.FloatField(blank=True, null=True, verbose_name='масса стакана i')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='массовая доля сырого жира')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='дата анализа')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fats', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Жир',
                'verbose_name_plural': 'Жир',
            },
        ),
    ]