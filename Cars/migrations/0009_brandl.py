# Generated by Django 4.0.3 on 2022-05-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0008_delete_brandlogos'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=20)),
            ],
        ),
    ]
