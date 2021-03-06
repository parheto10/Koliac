# Generated by Django 3.2.13 on 2022-07-13 09:13

from django.db import migrations, models
import django.utils.timezone
import parametres.models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='add_le',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='adresse',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ADRESSE'),
        ),
        migrations.AddField(
            model_name='user',
            name='contact1',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Contact'),
        ),
        migrations.AddField(
            model_name='user',
            name='contact2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='moov_money',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mtn_money',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nom',
            field=models.CharField(max_length=255, null=True, verbose_name='Nom et Pr??noms'),
        ),
        migrations.AddField(
            model_name='user',
            name='num_piece',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='N?? PIECE'),
        ),
        migrations.AddField(
            model_name='user',
            name='orange_money',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='piece',
            field=models.FileField(blank=True, null=True, upload_to=parametres.models.documents, verbose_name='DOCUMENT'),
        ),
        migrations.AddField(
            model_name='user',
            name='type_piece',
            field=models.CharField(blank=True, choices=[('AUCUN', 'AUCUN'), ('ATTESTATION', 'ATTESTATION'), ('CNI', 'CNI'), ('PASSEPORT', 'PASSEPORT'), ('SEJOUR', 'CARTE DE SEJOUR'), ('CONSULAIRE', 'CARTE CONSULAIRE')], default='CNI', max_length=50, null=True, verbose_name='TYPE DOCUMENT'),
        ),
        migrations.AddField(
            model_name='user',
            name='update_le',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
