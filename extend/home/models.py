# Import modules/packages
from django.db import models
from django.utils import timezone




# The main app
# This is a model called 'Extend' that represents the home/landing page of the app.
# It has three main attributes: 'name/ingin', 'source', and 'hot_prices'.
class Extend(models.Model):
    
    # 'name' is a short text describing this thing, like a product name.
    name = models.CharField(max_length=100)
    SOLAR = "SOLAR"
    WIND = "WIND"
    HYDRO = "HYDRO"
    GEOTHERMAL = "GEOTHERMAL"
    BIOGAS = "BIO-GAS"
    BIOFUEL = "BIO-FUEL"
    source_choices = [
        (SOLAR, 'Solar'),
        (WIND, 'Wind'),
        (HYDRO, 'Hydro'),
        (GEOTHERMAL, 'Geothermal'),
        (BIOGAS, 'Bio-gas'),
        (BIOFUEL, 'Bio-fuel')
    ]

     # 'source' is a dropdown choice field for the energy source (like solar or wind).
    source = models.CharField(max_length=50, choices=source_choices, default=SOLAR,)

    # 'hot_prices' is a number field representing the cost of the current energy. 
    # It has to be changing every second like crytocurrency prices
    hot_prices = models.DecimalField(max_digits=5, decimal_places=2)
    

    # Refer to this object, to show its 'name'.
    def __str__(self):
        return self.name
    

    # Query to sort based on their 'hot_prices'.
    class Meta:
        ordering = ['hot_prices']

# Powerwall definition
# This is another model called 'Overdrive', representing the powerwall page.
class Overdrive(models.Model):

    # Users Dashboard
    capacity_choices = [
        ('5 kWh', '5 kWh'),
        ('10 kWh', '10 kWh'),
        ('15 kWh', '15 kWh'),
    ]
    capacity = models.CharField(max_length=10, choices=capacity_choices, default='5 kWh')
    
    charging_speed_choices = [
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
   

    def update_energy_consumption(self, energy_consumption):
        self.current_energy_consumption = energy_consumption
        self.last_updated = timezone.now()
        self.save()

    def update_energy_production(self, energy_production):
        self.current_energy_production = energy_production
        self.last_production_update = timezone.now()
        self.save()

    def update_energy_consumption(self, energy_consumption):
        self.current_energy_consumption = energy_consumption
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

    # New fields for Producer Dashboard/features
    producer_dashboard_feature = models.BooleanField(default=False)
    individual_system_monitoring = models.BooleanField(default=False)
    performance_analysis = models.BooleanField(default=False)
    system_health_alerts = models.BooleanField(default=False)
    weather_integration = models.BooleanField(default=False)
    producer_battery_management = models.BooleanField(default=False)
    environmental_impact_report = models.BooleanField(default=False)
    energy_usage_insight = models.BooleanField(default=False)
    performance_improvement = models.BooleanField(default=False)
    regulatory_compliance = models.BooleanField(default=False)
    renewable_energy_certificate_integration = models.BooleanField(default=False)
    data_privacy_security = models.BooleanField(default=False)
    user_support = models.BooleanField(default=False)
    documentation_resources = models.BooleanField(default=False)

    # Additional fields for Producer Information
    producer_name = models.CharField(max_length=100, default="")
    renewable_energy_type = models.CharField(max_length=50, default="")
    producer_location = models.CharField(max_length=100, default="")
    
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


    # Overall Overdrive command
    def __str__(self):
        # Refer to this object, to show its 'capacity' and 'charging_speed'.
        return f"Overdrive - {self.capacity}, {self.charging_speed}"


# Ecommerce
# 'Hormone' representing as an ecommerce system.
class Hormone(models.Model):
    #  Users
    name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")

    
    
    
    # Dashboard features for producers
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    rating = models.FloatField(default=0.0) 
    energy_type = models.CharField(max_length=100, default="")
    renewable_energy_source = models.ManyToManyField('self', blank=True, symmetrical=False)
    storage_capacity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    promotions = models.TextField(blank=True)
    orders = models.PositiveIntegerField(default=0)
    management_and_processes = models.TextField(blank=True)


    # Refer to this product, to show its 'name'.
    def __str__(self):
        return self.name


