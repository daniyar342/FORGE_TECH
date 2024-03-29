# Generated by Django 4.2 on 2024-01-27 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appartments', '0002_alter_city_options_alter_client_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='clients',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appartments.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appartments.city', verbose_name='Обьект'),
        ),
    ]
