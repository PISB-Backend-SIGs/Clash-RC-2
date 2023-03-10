# Generated by Django 4.1.6 on 2023-02-12 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('p_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('p_score', models.IntegerField(default=0)),
                ('p_is_started', models.BooleanField(default=False)),
                ('p_start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.IntegerField(primary_key=True, serialize=False)),
                ('q_title', models.CharField(max_length=40)),
                ('q_descrp', models.TextField()),
                ('q_ip_formate', models.TextField(null=True)),
                ('q_op_formate', models.TextField(null=True)),
                ('q_const', models.TextField(null=True)),
                ('q_sip', models.TextField(null=True)),
                ('q_sop', models.TextField(null=True)),
                ('q_diff_level', models.CharField(max_length=50)),
                ('q_point', models.IntegerField(default=0)),
                ('q_aqrcy', models.IntegerField(default=0)),
                ('q_subns', models.IntegerField(default=0)),
                ('q_time_limit', models.IntegerField(null=True)),
                ('q_memory_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testcases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.IntegerField(null=True)),
                ('t_ip', models.TextField(null=True)),
                ('t_op', models.TextField(null=True)),
                ('q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.question')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.IntegerField(null=True)),
                ('s_code', models.TextField(null=True)),
                ('s_pt', models.IntegerField(default=0)),
                ('s_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.player')),
            ],
        ),
    ]
