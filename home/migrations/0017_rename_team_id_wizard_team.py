# Generated by Django 4.0.6 on 2022-10-17 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_wizard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wizard',
            old_name='team_id',
            new_name='team',
        ),
    ]
