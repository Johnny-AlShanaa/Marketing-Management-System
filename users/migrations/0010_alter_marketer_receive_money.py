# Generated by Django 4.0 on 2022-07-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_marketer_receive_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketer',
            name='receive_money',
            field=models.IntegerField(default=0),
        ),
    ]