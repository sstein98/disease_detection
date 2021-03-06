# Generated by Django 3.0.7 on 2020-06-11 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symptom', models.CharField(max_length=256)),
                ('PrevMeasure', models.CharField(max_length=512)),
                ('Plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Plant')),
            ],
        ),
    ]
