# Generated by Django 3.2.8 on 2021-11-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0004_auto_20211101_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matiere',
            old_name='nomMatiere',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matiere',
        ),
        migrations.AddField(
            model_name='note',
            name='matieres',
            field=models.ManyToManyField(to='bulletin.Matiere'),
        ),
    ]