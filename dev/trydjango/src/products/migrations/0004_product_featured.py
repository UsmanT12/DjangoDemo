# Generated by Django 2.1.7 on 2024-06-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20240624_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=2),
            preserve_default=False,
        ),
    ]
