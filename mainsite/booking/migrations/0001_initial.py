# Generated by Django 3.2.4 on 2021-06-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=250, verbose_name='Destination')),
                ('departureDate', models.DateField(verbose_name='Date de départ')),
                ('departureTime', models.CharField(max_length=5, verbose_name='Heure de départ')),
                ('sharing', models.CharField(max_length=3, verbose_name='Partage')),
                ('firstname', models.CharField(max_length=250, verbose_name='Prénom')),
                ('lastname', models.CharField(max_length=250, verbose_name='Nom de famille')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix')),
            ],
            options={
                'db_table': 'booking',
                'managed': True,
                'unique_together': {('destination', 'departureDate', 'email')},
            },
        ),
    ]
