# Generated by Django 4.0.4 on 2022-06-30 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='timetable',
            field=models.ImageField(blank=True, null=True, upload_to='calendar/'),
        ),
    ]