# Generated by Django 2.2.4 on 2019-12-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(default=0, max_length=400)),
                ('lastname', models.CharField(default=0, max_length=400)),
                ('email', models.CharField(default=0, max_length=400)),
                ('mobile', models.IntegerField(default=0)),
            ],
        ),
    ]
