# Generated by Django 2.0.2 on 2018-05-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_cocktail', '0008_auto_20180507_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='alc_percent',
            field=models.FloatField(default=0.0, null=True, verbose_name='度数(%)'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='unit_of_quantity',
            field=models.CharField(choices=[('ml', 'ml'), ('tsp', 'ティースプーン')], default='ml', max_length=4, null=True, verbose_name='分量単位'),
        ),
    ]
