# Generated by Django 4.2.4 on 2024-01-13 04:33

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_city_userprofile_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='energy_source',
            field=models.CharField(max_length=20, choices=[
                ('SOLAR', 'Solar'), 
                ('WIND', 'Wind'), 
                ('HYDRO', 'Hydro'), 
                ('GEOTHERMAL', 'Geothermal'), 
                ('BIO-GAS', 'Bio-gas'), 
                ('BIO-FUEL', 'Bio-fuel')
            ], 
            blank=True, null=True),
        ),
    ]
