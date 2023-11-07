# Generated by Django 4.2.6 on 2023-11-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('MNC', 'MNC'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('MEC', 'MEC'), ('CER', 'CER'), ('CHE', 'CHE'), ('CIV', 'CIV'), ('MET', 'MET'), ('MIN', 'MIN'), ('PHE', 'PHE'), ('APD', 'APD')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='semester',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=10, null=True),
        ),
    ]