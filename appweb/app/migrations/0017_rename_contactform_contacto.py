# Generated by Django 5.0.7 on 2024-08-08 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_contactform_mensaje'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contactform',
            new_name='Contacto',
        ),
    ]