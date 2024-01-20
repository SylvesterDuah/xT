# Generated by Django 4.2.4 on 2024-01-14 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hormone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('hormone_image', models.ImageField(blank=True, null=True, upload_to='hormone/')),
                ('models_and_specifications', models.TextField(blank=True, null=True)),
                ('key_benefits', models.TextField(blank=True, null=True)),
                ('getting_started_guide', models.TextField(blank=True, null=True)),
                ('renewable_energy_stores', models.TextField(blank=True, null=True)),
                ('pricing_information', models.TextField(blank=True, null=True)),
                ('sustainability_commitment', models.TextField(blank=True, null=True)),
                ('login_signup_prompt', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HormoneUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('type_of_energy', models.CharField(default='', max_length=100)),
                ('rating', models.FloatField(default=0.0)),
                ('source', models.CharField(blank=True, choices=[], max_length=20)),
                ('deals_of_the_week', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HormoneProducer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storefront', models.CharField(default='', max_length=100)),
                ('engine_type', models.CharField(default='', max_length=100)),
                ('storage', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('promotions', models.TextField(blank=True)),
                ('customer_orders', models.PositiveIntegerField(default=0)),
                ('management', models.TextField(blank=True)),
                ('integration', models.TextField(blank=True)),
                ('total_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_tenure', models.PositiveIntegerField(default=0)),
                ('reports', models.TextField(blank=True)),
                ('contributions_to_ecosystem', models.TextField(blank=True)),
                ('analytics', models.TextField(blank=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]