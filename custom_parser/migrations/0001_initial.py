# Generated by Django 2.2.dev20190103234849 on 2019-01-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.TextField(default='1.0')),
            ],
            options={
                'db_table': 'videos',
            },
        ),
    ]