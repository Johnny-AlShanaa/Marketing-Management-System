# Generated by Django 4.0 on 2022-07-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_promotion_money_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketer',
            name='receive_money',
            field=models.IntegerField(null=True),
        ),
    ]