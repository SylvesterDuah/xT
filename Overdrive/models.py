# Overdrive/models.py

# Powerwall definition
from django.db import models
from django.utils import timezone


# overdrive/models.py

from django.db import models


# Features for Powerwall Main Page (Without Login)
class Overdrive(models.Model):
    
    # Display general information about Powerwall
    description = models.TextField(blank=True, null=True)

    # Image field for adding a main page image
    overdrive_image = models.ImageField(upload_to='overdrive/', null=True, blank=True)
    
    
    
    # Display available models and their specifications
    models_and_specifications = models.TextField(blank=True, null=True)
    
    # Highlight key benefits of using Powerwall
    key_benefits = models.TextField(blank=True, null=True)
    
    # Provide information on how to get started with Powerwall
    getting_started_guide = models.TextField(blank=True, null=True)
    
    # Display pricing information or link to pricing details
    pricing_information = models.TextField(blank=True, null=True)
    
    # Showcase customer testimonials or success stories
    customer_testimonials = models.TextField(blank=True, null=True)
    
    # Display information about Overdrive's commitment to sustainability
    sustainability_commitment = models.TextField(blank=True, null=True)
    
    # Include a call-to-action for users to log in or sign up
    login_signup_prompt = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "Overdrive"





# This is another model called 'OverdriveUser', representing the powerwall page.
class OverdriveUser(models.Model):
    # Users Dashboard
    capacity_choices = [
        ('5 kWh', '5 kWh'),
        ('10 kWh', '10 kWh'),
        ('15 kWh', '15 kWh'),
    ]
    capacity = models.CharField(max_length=10, choices=capacity_choices, default='5 kWh')

    charging_speed_choices = [
        ('Very Slow', 'Very Slow'),
        ('Slow', 'Slow'),
        ('Standard', 'Standard'),
        ('Fast', 'Fast'),
        ('Ultra Fast', 'Ultra Fast')
    ]
    charging_speed = models.CharField(max_length=20, choices=charging_speed_choices, default='Standard')
    voltage = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    # Fields for additional features
    customer_name = models.CharField(max_length=100, default="")
    order_date = models.DateField(default=timezone.now)
    available_quantity = models.PositiveIntegerField(default=0)
    support_email = models.EmailField(max_length=254, default="")
    customer_service_number = models.CharField(max_length=20, default="")

    # Fields for promotions and marketing
    promotional_code = models.CharField(max_length=20, blank=True)
    marketing_message = models.TextField(blank=True)

    # Fields for data analysis
    power_usage_data = models.JSONField(blank=True, null=True)
    storage_capacity_data = models.JSONField(blank=True, null=True)

    # Additional fields for Energy Tracking
    energy_tracking_feature = models.BooleanField(default=False)

    # Additional fields for Real-Time Energy Data
    current_energy_consumption = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    # Additional fields for Energy Production Monitoring
    energy_production_monitoring_feature = models.BooleanField(default=False)

    # Additional fields for Real-Time Energy Production Monitoring
    current_energy_production = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_production_update = models.DateTimeField(null=True, blank=True)

    # Additional fields for Smart Energy Management
    smart_energy_management_feature = models.BooleanField(default=False)
    current_energy_consumption = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    energy_saving_mode = models.BooleanField(default=False)

    # Additional fields for Battery Management
    battery_management_feature = models.BooleanField(default=False)
    battery_charge_level = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    battery_health_status = models.CharField(max_length=20, choices=[
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor')
    ], blank=True)

    # Additional fields for Sustainability Insights
    sustainability_insights_feature = models.BooleanField(default=False)
    carbon_emissions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    energy_efficiency_rating = models.CharField(max_length=20, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ], blank=True)

    # Additional fields for Home Automation
    home_automation_feature = models.BooleanField(default=False)

    # Additional fields for Renewable Energy Incentives
    renewable_energy_incentives_feature = models.BooleanField(default=False)

    # Additional fields for Smart Meters
    smart_meters_feature = models.BooleanField(default=False)

    # Fields for recent activity
    activity_date = models.DateTimeField(default=timezone.now)
    activity_type = models.CharField(max_length=100, default='Default Activity Type')
    activity_details = models.TextField(default='Default activity details')

    # Additional fields for Integration
    integration_feature = models.BooleanField(default=False)

    # Additional fields for Multi-platforms
    multi_platform_feature = models.BooleanField(default=False)

    # Additional fields for Community Engagement
    community_engagement_feature = models.BooleanField(default=False)

    # Additional fields for Energy Forecast News
    energy_forecast_news_feature = models.BooleanField(default=False)
    energy_forecast_news = models.TextField(blank=True)

    def update_energy_consumption(self, energy_consumption):
        self.current_energy_consumption = energy_consumption
        self.last_updated = timezone.now()
        self.save()

    def update_energy_production(self, energy_production):
        self.current_energy_production = energy_production
        self.last_production_update = timezone.now()
        self.save()

    def set_energy_saving_mode(self, enable):
        self.energy_saving_mode = enable
        self.save()

    def update_battery_charge_level(self, charge_level):
        self.battery_charge_level = charge_level
        self.save()

    def update_battery_health_status(self, health_status):
        self.battery_health_status = health_status
        self.save()

    def update_carbon_emissions(self, emissions):
        self.carbon_emissions = emissions
        self.save()

    def update_energy_efficiency_rating(self, efficiency_rating):
        self.energy_efficiency_rating = efficiency_rating
        self.save()

    environmental_impact_report = models.BooleanField(default=False)
    energy_usage_insight = models.BooleanField(default=False)
    performance_improvement = models.BooleanField(default=False)
    regulatory_compliance = models.BooleanField(default=False)
    renewable_energy_certificate_integration = models.BooleanField(default=False)
    data_privacy_security = models.BooleanField(default=False)
    user_support = models.BooleanField(default=False)
    documentation_resources = models.BooleanField(default=False)

    # Additional fields for Sales Information
    sales_spending = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    # New fields for Sales Dashboard - producers
    sales_dashboard_feature = models.BooleanField(default=False)

    spending_financial_reporting = models.BooleanField(default=False)

    def update_individual_system_monitoring(self, enable):
        self.individual_system_monitoring = enable
        self.save()

    def update_performance_analysis(self, enable):
        self.performance_analysis = enable
        self.save()

    def update_system_health_alerts(self, enable):
        self.system_health_alerts = enable
        self.save()

    def update_spending_financial_reporting(self, enable):
        self.earnings_financial_reporting = enable
        self.save()

    def update_energy_forecast_news(self, news):
        self.energy_forecast_news = news
        self.save()

    def __str__(self):
        return f"OverdriveUser - {self.capacity}, {self.charging_speed}"


class OverdriveProducer(models.Model):
    # Users Dashboard
    capacity_choices = [
        ('5 kWh', '5 kWh'),
        ('10 kWh', '10 kWh'),
        ('15 kWh', '15 kWh'),
    ]
    capacity = models.CharField(max_length=10, choices=capacity_choices, default='5 kWh')

    charging_speed_choices = [
        ('Very Slow', 'Very Slow'),
        ('Slow', 'Slow'),
        ('Standard', 'Standard'),
        ('Fast', 'Fast'),
        ('Ultra Fast', 'Ultra Fast')
    ]
    charging_speed = models.CharField(max_length=20, choices=charging_speed_choices, default='Standard')
    voltage = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    # Fields for additional features
    producer_name = models.CharField(max_length=100, default="")
    order_date    = models.DateField(default=timezone.now)
    available_quantity = models.PositiveIntegerField(default=0)
    support_email = models.EmailField(max_length=254, default="")
    customer_service_number = models.CharField(max_length=20, default="")

    # Fields for data analysis
    power_usage_data = models.JSONField(blank=True, null=True)
    storage_capacity_data = models.JSONField(blank=True, null=True)

    # Additional fields for Energy Tracking
    energy_tracking_feature = models.BooleanField(default=False)

    # Additional fields for Real-Time Energy Data
    current_energy_consumption = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    # Additional fields for Energy Production Monitoring
    energy_production_monitoring_feature = models.BooleanField(default=False)

    # Additional fields for Real-Time Energy Production Monitoring
    current_energy_production = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_production_update = models.DateTimeField(null=True, blank=True)

    # Additional fields for Smart Energy Management
    smart_energy_management_feature = models.BooleanField(default=False)
    current_energy_consumption = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    energy_saving_mode = models.BooleanField(default=False)

    # Additional fields for Battery Management
    battery_management_feature = models.BooleanField(default=False)
    battery_charge_level = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    battery_health_status = models.CharField(max_length=20, choices=[
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor')
    ], blank=True)

    # Additional fields for Sustainability Insights
    sustainability_insights_feature = models.BooleanField(default=False)
    carbon_emissions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    energy_efficiency_rating = models.CharField(max_length=20, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ], blank=True)

    # Additional fields for Home Automation
    home_automation_feature = models.BooleanField(default=False)

    # Additional fields for Renewable Energy Incentives
    renewable_energy_incentives_feature = models.BooleanField(default=False)

    # Additional fields for Smart Meters
    smart_meters_feature = models.BooleanField(default=False)

    # Fields for recent activity
    activity_date = models.DateTimeField(default=timezone.now)
    activity_type = models.CharField(max_length=100, default='Default Activity Type')
    activity_details = models.TextField(default='Default activity details')

    # Additional fields for Integration
    integration_feature = models.BooleanField(default=False)

    # Additional fields for Community Engagement
    community_engagement_feature = models.BooleanField(default=False)

    # Additional fields for Energy Forecast News
    energy_forecast_news_feature = models.BooleanField(default=False)
    energy_forecast_news = models.TextField(blank=True)

    def update_energy_consumption(self, energy_consumption):
        self.current_energy_consumption = energy_consumption
        self.last_updated = timezone.now()
        self.save()

    def update_energy_production(self, energy_production):
        self.current_energy_production = energy_production
        self.last_production_update = timezone.now()
        self.save()

    def set_energy_saving_mode(self, enable):
        self.energy_saving_mode = enable
        self.save()

    def update_battery_charge_level(self, charge_level):
        self.battery_charge_level = charge_level
        self.save()

    def update_battery_health_status(self, health_status):
        self.battery_health_status = health_status
        self.save()

    def update_carbon_emissions(self, emissions):
        self.carbon_emissions = emissions
        self.save()

    def update_energy_efficiency_rating(self, efficiency_rating):
        self.energy_efficiency_rating = efficiency_rating
        self.save()

    # Additional fields for Sales Information
    sales_earnings = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    # New fields for Sales Dashboard - producers
    sales_dashboard_feature = models.BooleanField(default=False)

    earnings_financial_reporting = models.BooleanField(default=False)

    def update_individual_system_monitoring(self, enable):
        self.individual_system_monitoring = enable
        self.save()

    def update_performance_analysis(self, enable):
        self.performance_analysis = enable
        self.save()

    def update_system_health_alerts(self, enable):
        self.system_health_alerts = enable
        self.save()

    def update_earnings_financial_reporting(self, enable):
        self.earnings_financial_reporting = enable
        self.save()

    def update_energy_forecast_news(self, news):
        self.energy_forecast_news = news
        self.save()

    def __str__(self):
        return f"OverdriveProducer - {self.capacity}, {self.charging_speed}"

