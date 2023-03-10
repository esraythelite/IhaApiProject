# Generated by Django 4.1.5 on 2023-01-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iha',
            fields=[
                ('IhaId', models.AutoField(primary_key=True, serialize=False)),
                ('IhaBrand', models.CharField(max_length=150)),
                ('IhaModel', models.CharField(max_length=200)),
                ('IhaCategory', models.CharField(max_length=150)),
                ('IhaWeight', models.BigIntegerField()),
                ('IhaLength', models.BigIntegerField()),
                ('IhaProductionDate', models.DateField()),
                ('IhaPhotoFileName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=200)),
            ],
        ),
    ]
