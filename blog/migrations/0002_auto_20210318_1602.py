# Generated by Django 3.1.2 on 2021-03-18 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigo',
            options={'ordering': ['-submitted']},
        ),
        migrations.AddField(
            model_name='artigo',
            name='submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artigo',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
