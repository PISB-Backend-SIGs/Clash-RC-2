# Generated by Django 4.2 on 2023-05-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_question_isforjuniors'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionNumber',
            field=models.IntegerField(null=True),
        ),
    ]