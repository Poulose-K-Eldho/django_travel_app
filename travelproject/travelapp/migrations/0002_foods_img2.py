# Generated by Django 3.2 on 2021-04-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='img2',
            field=models.ImageField(default='hi.jpg', upload_to='picture'),
            preserve_default=False,
        ),
    ]
