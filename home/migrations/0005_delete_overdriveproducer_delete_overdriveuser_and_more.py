# Generated by Django 4.2.4 on 2024-01-13 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_hormoneproducer_hormoneuser_overdriveproducer_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OverdriveProducer',
        ),
        migrations.DeleteModel(
            name='OverdriveUser',
        ),
        migrations.AlterField(
            model_name='hormoneproducer',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]