# Generated by Django 5.0.3 on 2024-03-25 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
