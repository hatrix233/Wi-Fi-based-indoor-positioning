# Generated by Django 2.1.4 on 2019-06-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0005_auto_20190528_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='picture',
            field=models.CharField(default='1.jpg', max_length=16, verbose_name='结构图'),
        ),
    ]
