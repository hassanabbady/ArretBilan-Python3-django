# Generated by Django 3.2.8 on 2021-11-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0005_auto_20211103_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eleve',
            old_name='nompre',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='note',
            name='eleve',
        ),
        migrations.AddField(
            model_name='note',
            name='eleves',
            field=models.ManyToManyField(to='bulletin.Eleve'),
        ),
    ]
