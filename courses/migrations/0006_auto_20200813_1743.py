# Generated by Django 3.0.8 on 2020-08-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_flyer_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='flyer_img',
            field=models.ImageField(blank=True, default='images/default1.png', null=True, upload_to='images'),
        ),
    ]
