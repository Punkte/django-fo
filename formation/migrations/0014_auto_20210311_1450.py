# Generated by Django 3.1.7 on 2021-03-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0013_cv_experiences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='experiences',
            field=models.TextField(blank=True, null=True),
        ),
    ]