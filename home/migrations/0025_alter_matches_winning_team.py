# Generated by Django 4.0.6 on 2022-11-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_matches_winning_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='winning_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='home.teams'),
        ),
    ]
