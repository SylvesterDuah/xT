# ** Docummentation **
# This form is created for the Extend model, Overdrive, and the Hormone
# The Extend Form: 
# It specifies that the form should include the 
# fields name, source, and hot_prices from the Extend model

# The subform:
# TIt include only a subset of fields from the Extend model. 
# InginForm has only the name field
# HotPriceForm includes only the hot_prices field
# SourceForm includes only the source field

# Overdrive form:
# It includes a list of fields specific to the Overdrive model.

# Hormone form:
# It includes a list of fields specific to the Hormone model.


# Import modules/packages
from django import forms
from django.forms import formset_factory


# Importing the models
from .models import Extend, Overdrive, Hormone




# Extend page form 
class ExtendForm(forms.ModelForm):
    class Meta:
        model = Extend
        fields = ['name', 'source', 'hot_prices']


# Form for 'name/ingine' field only
class InginForm(forms.ModelForm):
    class Meta:
        model = Extend
        fields = ['name']


# Form for 'hot_prices' field only
class HotPriceForm(forms.ModelForm):
    class Meta:
        model = Extend
        fields = ['hot_prices']


# Form for 'source' field only
class SourceForm(forms.ModelForm):
    class Meta:
        model = Extend
        fields = ['source']

# Create formsets
InginFormSet = formset_factory(InginForm, extra=1)
HotPriceFormSet = formset_factory(HotPriceForm, extra=1)
SourceFormSet = formset_factory(SourceForm, extra=1)






# Overdrive form page
class OverdriveForm(forms.ModelForm):
    class Meta:
        model = Overdrive
        fields = [
            'capacity',
            'charging_speed',
            'voltage',
            'customer_name',
            'order_date',
            'support_email',
            'customer_service_number',
            'promotional_code',
            'marketing_message',
            'power_usage_data',
            'storage_capacity_data',
            'energy_tracking_feature',
            'current_energy_consumption',
            'energy_production_monitoring_feature',
            'current_energy_production',
            'smart_energy_management_feature',
            'energy_saving_mode',
            'battery_management_feature',
            'battery_charge_level',
            'battery_health_status',
            'sustainability_insights_feature',
            'carbon_emissions',
            'energy_efficiency_rating',
            'home_automation_feature',
            'renewable_energy_incentives_feature',
            'smart_meters_feature',
            'activity_date',
            'activity_type',
            'activity_details',
            'integration_feature',
            'multi_platform_feature',
            'community_engagement_feature',
            'energy_forecast_news_feature',
            'producer_dashboard_feature',
            'individual_system_monitoring',
            'performance_analysis',
            'system_health_alerts',
            'weather_integration',
            'producer_battery_management',
            'environmental_impact_report',
            'energy_usage_insight',
            'performance_improvement',
            'regulatory_compliance',
            'renewable_energy_certificate_integration',
            'data_privacy_security',
            'user_support',
            'documentation_resources',
            'producer_name',
            'renewable_energy_type',
            'producer_location',
            'sales_earnings',
            'sales_dashboard_feature',
            'earnings_financial_reporting',
        ]



# Hormone form page
class HormoneForm(forms.ModelForm):
    class Meta:
        model = Hormone
        fields = [
            'name',
            'location',
            'description',
            'price',
            'rating',
            'energy_type',
            'renewable_energy_source',
            'storage_capacity',
            'promotions',
            'orders',
            'management_and_processes',
        ]
