# Generated by Django 3.1.2 on 2020-10-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=2, unique=True, verbose_name='Nombre corto'),
        ),
    ]
