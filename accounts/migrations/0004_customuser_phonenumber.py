# Generated by Django 3.1 on 2020-08-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
