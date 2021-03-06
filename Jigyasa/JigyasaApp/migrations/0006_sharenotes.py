# Generated by Django 3.2.8 on 2021-11-08 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JigyasaApp', '0005_auto_20211108_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareNotes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(default='', max_length=100)),
                ('notes', models.FileField(upload_to='media/Notes')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JigyasaApp.staffs')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JigyasaApp.subjects')),
            ],
        ),
    ]
