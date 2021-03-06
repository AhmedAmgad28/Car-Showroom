# Generated by Django 4.0.3 on 2022-05-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0005_brandlogos_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='brand',
            field=models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('BYD', 'BYD'), ('Chery', 'Chery'), ('Chevrolet', 'Chevrolet'), ('Citroën', 'Citroën'), ('Daewoo', 'Daewoo'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Geely', 'Geely'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lada', 'Lada'), ('Land Rover', 'Land Rover'), ('Mercedes', 'Mercedes'), ('MG', 'MG'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Skoda', 'Skoda'), ('Speranza', 'Speranza'), ('Toyota', 'Toyota'), ('Volvo', 'Volvo'), ('Other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='usedcar',
            name='brand',
            field=models.CharField(choices=[('Audi', 'Audi'), ('BMW', 'BMW'), ('BYD', 'BYD'), ('Chery', 'Chery'), ('Chevrolet', 'Chevrolet'), ('Citroën', 'Citroën'), ('Daewoo', 'Daewoo'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Geely', 'Geely'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lada', 'Lada'), ('Land Rover', 'Land Rover'), ('Mercedes', 'Mercedes'), ('MG', 'MG'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Skoda', 'Skoda'), ('Speranza', 'Speranza'), ('Toyota', 'Toyota'), ('Volvo', 'Volvo'), ('Other', 'Other')], max_length=20),
        ),
    ]
