# Generated by Django 4.2.5 on 2023-09-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthGuide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='Doctor', max_length=100),
            preserve_default=False,
        ),
    ]
