# Generated by Django 3.2.12 on 2022-02-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0003_promotion_key_prom'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='prom_name',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]