# Generated by Django 3.1.5 on 2021-01-27 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификация',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('bg', models.CharField(max_length=50)),
                ('btn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Цвет этикетки',
                'verbose_name_plural': 'Цвет этикетки',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='место отбора пробы', max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компания',
            },
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Тип образца',
                'verbose_name_plural': 'Тип образца',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукт',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.SlugField(unique=True, verbose_name='образец')),
                ('date_production', models.DateField(verbose_name='дата производства')),
                ('bb_from', models.PositiveIntegerField(blank=True, null=True, verbose_name='Б.Б с')),
                ('bb_to', models.PositiveIntegerField(blank=True, null=True, verbose_name='Б.Б по')),
                ('pallet_from', models.PositiveIntegerField(blank=True, null=True, verbose_name='паллеты с')),
                ('pallet_to', models.PositiveIntegerField(blank=True, null=True, verbose_name='паллеты по')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание')),
                ('date_registration', models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')),
                ('repeate', models.BooleanField(verbose_name='повтор')),
                ('claim', models.BooleanField(verbose_name='претензия')),
                ('comment', models.TextField(blank=True, verbose_name='комментарий')),
                ('category', models.ManyToManyField(blank=True, related_name='samples', to='lims.Category', verbose_name='спецификация')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lims.color', verbose_name='цвет этикетки')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims.company', verbose_name='компания')),
                ('material_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims.materialtype', verbose_name='вид образца')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lims.producttype', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Образец',
                'verbose_name_plural': 'Образцы',
            },
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_mass', models.FloatField(blank=True, max_length=5, null=True, verbose_name='масса навески')),
                ('titrant_volume', models.FloatField(blank=True, null=True, verbose_name='объем 0.2 М серной кислоты')),
                ('value', models.FloatField(blank=True, max_length=4, null=True, verbose_name='массовая доля сырого протеина')),
                ('date_pub', models.DateTimeField(auto_now=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proteins', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Протеин',
                'verbose_name_plural': 'Протеин',
            },
        ),
        migrations.CreateModel(
            name='Moisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blank_cup_mass', models.FloatField(blank=True, null=True, verbose_name='масса пустой бюксы')),
                ('sample_mass', models.FloatField(blank=True, null=True, verbose_name='масса навески')),
                ('final_cup_mass', models.FloatField(blank=True, null=True, verbose_name='масса бюксы i')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='массовая доля влаги')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='дата анализа')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moistures', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Влага',
                'verbose_name_plural': 'Влага',
            },
        ),
        migrations.CreateModel(
            name='FFA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_mass', models.FloatField(blank=True, max_length=5, null=True, verbose_name='масса навески')),
                ('titrant_volume', models.FloatField(blank=True, null=True, verbose_name='объем 0.1 Н KOH')),
                ('value', models.FloatField(blank=True, max_length=4, null=True, verbose_name='кислотное число')),
                ('date_pub', models.DateTimeField(auto_now=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ffas', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Кислотное число',
                'verbose_name_plural': 'Кислотное число',
            },
        ),
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
        migrations.CreateModel(
            name='Bruker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ffa', models.FloatField(blank=True, null=True, verbose_name='кислотное число')),
                ('protein', models.FloatField(blank=True, null=True, verbose_name='протеин')),
                ('fat', models.FloatField(blank=True, null=True, verbose_name='жир')),
                ('ash', models.FloatField(blank=True, null=True, verbose_name='зола')),
                ('moisture', models.FloatField(blank=True, null=True, verbose_name='влага')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='дата анализа')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brukers', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Спектрометр',
                'verbose_name_plural': 'Спектрометр',
            },
        ),
        migrations.CreateModel(
            name='Ash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blank_cup_mass', models.FloatField(blank=True, null=True, verbose_name='масса пустого тигля')),
                ('sample_mass', models.FloatField(blank=True, null=True, verbose_name='масса навески')),
                ('final_cup_mass', models.FloatField(blank=True, null=True, verbose_name='масса тигля i')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='массовая доля сырой золы')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='дата анализа')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ashs', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Зола',
                'verbose_name_plural': 'Зола',
            },
        ),
        migrations.CreateModel(
            name='Aoks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_mass', models.FloatField(blank=True, null=True, verbose_name='масса навески')),
                ('bha', models.FloatField(blank=True, null=True)),
                ('bht', models.FloatField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True, verbose_name='суммарно bha/bht')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='дата анализа')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aoks', to='lims.sample', verbose_name='образец')),
            ],
            options={
                'verbose_name': 'Антиоксидант',
                'verbose_name_plural': 'Антиоксидант',
            },
        ),
    ]
