# Generated by Django 3.2.4 on 2021-06-23 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorias',
            old_name='descripcion',
            new_name='categoria',
        ),
    ]