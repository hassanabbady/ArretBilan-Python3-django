# Generated by Django 3.2.8 on 2021-11-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0014_alter_eleve_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='nomClasse',
            field=models.CharField(max_length=190, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='name',
            field=models.CharField(max_length=190, null=True),
        ),
    ]
