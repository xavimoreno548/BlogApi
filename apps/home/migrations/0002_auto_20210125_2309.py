# Generated by Django 3.1.3 on 2021-01-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometext',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hometext',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
