# Generated by Django 3.1.1 on 2020-10-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0003_auto_20201029_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='ean',
            field=models.CharField(editable=False, max_length=15),
        ),
    ]
