# Generated by Django 3.1.6 on 2021-03-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
