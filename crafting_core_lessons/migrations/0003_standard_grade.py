# Generated by Django 2.2.7 on 2019-11-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafting_core_lessons', '0002_auto_20191112_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='grade',
            field=models.CharField(default='', max_length=20),
        ),
    ]
