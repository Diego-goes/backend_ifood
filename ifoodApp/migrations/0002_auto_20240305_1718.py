# Generated by Django 3.2.5 on 2024-03-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='emailUsu',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
