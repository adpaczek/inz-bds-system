# Generated by Django 4.1.2 on 2022-12-30 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0021_alter_accessrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrequest',
            name='status',
            field=models.CharField(blank=True, default='oczekująca', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]