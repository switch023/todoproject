# Generated by Django 3.0.8 on 2020-08-10 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'Q1(重要かつ緊急)'), ('info', 'Q2(重要)'), ('success', 'Q3(緊急)')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
