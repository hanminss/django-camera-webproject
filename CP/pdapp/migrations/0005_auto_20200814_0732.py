# Generated by Django 3.1 on 2020-08-14 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdapp', '0004_auto_20200814_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='pdname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pd_star', to='pdapp.product'),
        ),
    ]
