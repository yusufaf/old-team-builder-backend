# Generated by Django 4.1.6 on 2023-02-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teambuilder", "0003_alter_team_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="players",
            field=models.JSONField(default=dict),
        ),
    ]
