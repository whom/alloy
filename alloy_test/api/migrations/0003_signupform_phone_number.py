# Generated by Django 3.2.10 on 2022-01-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220101_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupform',
            name='phone_number',
            field=models.TextField(default=1111111111, max_length=10),
            preserve_default=False,
        ),
    ]
