# Generated by Django 4.0.4 on 2022-06-23 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_nombrecontacto_contacto_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('codigo', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=15)),
                ('codigo', models.IntegerField()),
                ('anio', models.IntegerField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.pelicula')),
            ],
        ),
    ]