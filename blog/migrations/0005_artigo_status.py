# Generated by Django 3.1.2 on 2021-03-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210320_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', help_text='Set to "published" to make this post publicly visible', max_length=10),
        ),
    ]
