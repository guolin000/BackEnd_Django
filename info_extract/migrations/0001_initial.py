# Generated by Django 4.2.19 on 2025-03-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('input_text', models.TextField()),
                ('result', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prediction_results',
            },
        ),
    ]
