# Generated by Django 3.1.3 on 2020-11-27 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField(max_length=100)),
            ],
        ),
    ]
