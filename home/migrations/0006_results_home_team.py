# Generated by Django 4.0.6 on 2022-07-08 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_results_options_alter_teams_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='home_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='home_team', to='home.teams'),
            preserve_default=False,
        ),
    ]
