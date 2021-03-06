# Generated by Django 3.2 on 2021-04-21 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(default='', max_length=1000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_catalog.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_catalog.user')),
            ],
        ),
    ]
