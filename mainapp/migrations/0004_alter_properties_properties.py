# Generated by Django 3.2 on 2023-02-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_properties_id_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='properties',
            field=models.ImageField(blank=True, null=True, upload_to='media/properties'),
        ),
    ]
