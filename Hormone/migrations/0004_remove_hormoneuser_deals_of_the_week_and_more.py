# Generated by Django 4.2.4 on 2024-01-25 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hormone', '0003_rename_engine_type_renewableenergytype_get_ingins_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hormoneuser',
            name='deals_of_the_week',
        ),
        migrations.RemoveField(
            model_name='hormoneuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hormoneuser',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='hormoneuser',
            name='source',
        ),
        migrations.RemoveField(
            model_name='hormoneuser',
            name='type_of_energy',
        ),
        migrations.AddField(
            model_name='hormoneuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,  # Remove this line to allow automatic default value
        ),
        migrations.CreateModel(
            name='SellerRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hormone.hormoneproducer')),
            ],
        ),
    ]
