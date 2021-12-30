# Generated by Django 3.0.3 on 2021-07-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('d_o_b', models.DateField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]