# Generated by Django 4.2.13 on 2024-07-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_cartitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='session_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
