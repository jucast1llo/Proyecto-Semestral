# Generated by Django 4.0.4 on 2022-06-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_nombrecontacto_contacto_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peliculaproducto',
            name='id',
        ),
        migrations.AlterField(
            model_name='peliculaproducto',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]