# Generated by Django 4.0.5 on 2022-06-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(default='proj.png', upload_to='images/'),
        ),
    ]