# Generated by Django 3.2 on 2021-06-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('operation', models.CharField(max_length=15)),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
                ('result', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
