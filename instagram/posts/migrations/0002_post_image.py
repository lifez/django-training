# Generated by Django 2.2.4 on 2019-08-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='posts'),
            preserve_default=False,
        ),
    ]