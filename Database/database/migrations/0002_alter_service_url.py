# Generated by Django 4.1.3 on 2022-11-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
