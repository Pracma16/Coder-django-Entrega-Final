# Generated by Django 5.0.3 on 2024-04-02 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesores',
            old_name='apellido',
            new_name='asignatura',
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(max_length=154),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]