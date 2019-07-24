# Generated by Django 2.2.3 on 2019-07-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default=0, max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
    ]