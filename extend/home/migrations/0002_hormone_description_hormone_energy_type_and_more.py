# Generated by Django 4.2.4 on 2023-09-11 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hormone',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='hormone',
            name='energy_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hormone',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hormone',
            name='management_and_processes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hormone',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hormone',
            name='orders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hormone',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='hormone',
            name='promotions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='hormone',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='hormone',
            name='renewable_energy_source',
            field=models.ManyToManyField(blank=True, to='home.hormone'),
        ),
        migrations.AddField(
            model_name='hormone',
            name='storage_capacity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='activity_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='activity_details',
            field=models.TextField(default='Default activity details'),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='activity_type',
            field=models.CharField(default='Default Activity Type', max_length=100),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='battery_charge_level',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='battery_health_status',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')], max_length=20),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='battery_management_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='capacity',
            field=models.CharField(choices=[('5 kWh', '5 kWh'), ('10 kWh', '10 kWh'), ('15 kWh', '15 kWh')], default='5 kWh', max_length=10),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='carbon_emissions',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='charging_speed',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Fast', 'Fast'), ('Ultra Fast', 'Ultra Fast')], default='Standard', max_length=20),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='community_engagement_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='current_energy_consumption',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='current_energy_production',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='customer_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='customer_service_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='data_privacy_security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='documentation_resources',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='earnings_financial_reporting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='energy_efficiency_rating',
            field=models.CharField(blank=True, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=20),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='energy_forecast_news_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='energy_production_monitoring_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='energy_saving_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='energy_tracking_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='energy_usage_insight',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='environmental_impact_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='home_automation_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='individual_system_monitoring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='integration_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='last_production_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='marketing_message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='multi_platform_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='performance_analysis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='performance_improvement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='power_usage_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='producer_battery_management',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='producer_dashboard_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='producer_location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='producer_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='promotional_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='regulatory_compliance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='renewable_energy_certificate_integration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='renewable_energy_incentives_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='renewable_energy_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='sales_dashboard_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='sales_earnings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='smart_energy_management_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='smart_meters_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='storage_capacity_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='support_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='sustainability_insights_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='system_health_alerts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='user_support',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='voltage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='overdrive',
            name='weather_integration',
            field=models.BooleanField(default=False),
        ),
    ]
