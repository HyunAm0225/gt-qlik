# Generated by Django 3.0.5 on 2020-06-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20200603_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
