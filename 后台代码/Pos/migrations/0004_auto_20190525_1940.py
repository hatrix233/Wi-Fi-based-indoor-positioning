# Generated by Django 2.1.4 on 2019-05-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0003_auto_20190525_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='bssid',
            field=models.CharField(max_length=17, verbose_name='BSSID'),
        ),
    ]
