# Generated by Django 4.1.2 on 2022-12-11 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_accessrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrequest',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]