# Generated by Django 4.0.6 on 2022-10-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_wizard_match_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='wizard',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
