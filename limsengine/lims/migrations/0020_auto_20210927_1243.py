# Generated by Django 3.2.7 on 2021-09-27 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims', '0019_auto_20210916_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aoks',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='ash',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='bruker',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='fat',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='ffa',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='moisture',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='protein',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='color',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='company',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='material_type',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='work_shift',
        ),
        migrations.DeleteModel(
            name='Specification',
        ),
        migrations.DeleteModel(
            name='Aoks',
        ),
        migrations.DeleteModel(
            name='Ash',
        ),
        migrations.DeleteModel(
            name='Bruker',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Fat',
        ),
        migrations.DeleteModel(
            name='FFA',
        ),
        migrations.DeleteModel(
            name='MaterialType',
        ),
        migrations.DeleteModel(
            name='Moisture',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
        migrations.DeleteModel(
            name='Protein',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
        migrations.DeleteModel(
            name='WorkShift',
        ),
    ]
