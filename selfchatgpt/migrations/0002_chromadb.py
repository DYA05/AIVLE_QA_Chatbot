# Generated by Django 5.0.6 on 2024-06-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfchatgpt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChromaDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256)),
                ('QA', models.CharField(max_length=256)),
            ],
        ),
    ]