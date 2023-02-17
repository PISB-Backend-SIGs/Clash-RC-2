# Generated by Django 4.1.6 on 2023-02-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_player_p_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_const',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_ip_formate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_memory_limit',
            field=models.IntegerField(default=50000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_op_formate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_sip',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_sop',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_time_limit',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
