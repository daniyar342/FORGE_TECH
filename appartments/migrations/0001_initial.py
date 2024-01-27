# Generated by Django 4.2 on 2024-01-27 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('deal', models.CharField(max_length=255, verbose_name='Договор')),
                ('status', models.CharField(choices=[('active', 'Активен'), ('booking', 'Бронь'), ('sold', 'Куплено'), ('barter', 'Бартер'), ('installment', 'Рассрочка'), ('canceled', 'Отмена')], max_length=50, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_apartment', models.IntegerField(verbose_name='№ квартиры')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('square', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='КВ')),
                ('date', models.DateField(verbose_name='Дата')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('status', models.CharField(choices=[('Активен', 'Активен'), ('Бронь', 'Бронь'), ('Куплено', 'Куплено'), ('Бартер', 'Бартер'), ('Рассрочка', 'Рассрочка'), ('Отмена', 'Отмена')], max_length=50, verbose_name='Cтатус')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appartments.client', verbose_name='Клиент')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appartments.city', verbose_name='Обьект')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
            },
        ),
    ]
