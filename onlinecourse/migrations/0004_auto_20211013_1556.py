# Generated by Django 3.1.3 on 2021-10-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20211013_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(default='Available Instructor', to='onlinecourse.Instructor'),
        ),
    ]