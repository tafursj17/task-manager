# Generated by Django 4.1.5 on 2023-02-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_note_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(),
        ),
    ]