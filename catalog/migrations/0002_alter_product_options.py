# Generated by Django 5.0.3 on 2024-04-25 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id', 'name'), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
