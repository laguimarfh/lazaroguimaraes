# Generated by Django 3.1.2 on 2021-03-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210318_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='author',
            field=models.CharField(default='0', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artigo',
            name='destaque',
            field=models.BooleanField(null=True),
        ),
    ]
