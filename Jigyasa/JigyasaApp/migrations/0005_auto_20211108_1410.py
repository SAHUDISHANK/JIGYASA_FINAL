# Generated by Django 3.2.8 on 2021-11-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JigyasaApp', '0004_alter_leavereportstudent_leave_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='students',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
    ]
