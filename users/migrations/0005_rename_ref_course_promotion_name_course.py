# Generated by Django 4.0.6 on 2022-07-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_promotion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promotion',
            old_name='ref_course',
            new_name='name_course',
        ),
    ]