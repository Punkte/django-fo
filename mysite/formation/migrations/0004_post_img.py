# Generated by Django 3.1.7 on 2021-03-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0003_auto_20210309_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
