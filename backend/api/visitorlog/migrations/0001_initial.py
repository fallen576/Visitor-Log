# Generated by Django 3.2.7 on 2021-09-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
    ]
