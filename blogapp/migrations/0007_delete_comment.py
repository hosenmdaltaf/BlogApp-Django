# Generated by Django 3.0 on 2021-05-08 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
