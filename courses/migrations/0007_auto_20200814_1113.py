# Generated by Django 3.0.8 on 2020-08-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200813_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='flyer_img',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images'),
        ),
    ]