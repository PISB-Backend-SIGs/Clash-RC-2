# Generated by Django 4.1.6 on 2023-02-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_player_p_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='p_start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
