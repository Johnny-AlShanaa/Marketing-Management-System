# Generated by Django 4.0 on 2022-07-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_name_course_promotion_ref_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='ref_course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='ref_user',
            field=models.CharField(max_length=100),
        ),
    ]