# Generated by Django 3.2 on 2021-04-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_catalog', '0003_auto_20210421_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
