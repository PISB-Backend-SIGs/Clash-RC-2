# Generated by Django 4.1.6 on 2023-02-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_player_p_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='p_start_time',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
