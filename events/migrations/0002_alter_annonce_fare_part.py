# Generated by Django 3.2.13 on 2022-07-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='fare_part',
            field=models.FileField(blank=True, null=True, upload_to='faire_parts/', verbose_name='Faire Part'),
        ),
    ]
