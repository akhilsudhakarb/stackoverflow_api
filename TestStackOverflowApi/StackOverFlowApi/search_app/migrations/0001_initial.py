# Generated by Django 3.2.6 on 2021-08-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=300)),
                ('vote_count', models.IntegerField(default=0)),
                ('views', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=250)),
            ],
        ),
    ]