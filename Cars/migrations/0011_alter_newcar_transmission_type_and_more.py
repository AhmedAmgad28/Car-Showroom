# Generated by Django 4.0.3 on 2022-05-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0010_alter_transmission_transmission_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='transmission_type',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=20),
        ),
        migrations.AlterField(
            model_name='rentcar',
            name='transmission_type',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=20),
        ),
        migrations.AlterField(
            model_name='usedcar',
            name='transmission_type',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=20),
        ),
    ]
