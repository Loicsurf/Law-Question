# Generated by Django 3.1.7 on 2022-03-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_auto_20220314_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
