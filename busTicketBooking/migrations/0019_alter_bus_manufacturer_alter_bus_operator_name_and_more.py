# Generated by Django 4.0.4 on 2022-04-19 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busTicketBooking', '0018_passenger_reservation_reservationseat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='manufacturer',
            field=models.CharField(choices=[('SCANIA', 'Scania'), ('VOLVO', 'Volvo'), ('WRIGHTBUS', 'Wrightbus')], default='HINO', max_length=50),
        ),
        migrations.AlterField(
            model_name='bus',
            name='operator_name',
            field=models.CharField(choices=[('Ireland Express', 'Ireland Express'), ('Dublin Bus', 'Dublin Bus'), ('IRL Citylink', 'IRL Citylink')], default='...', max_length=50),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(choices=[('GALWAY', 'galway'), ('CORK', 'Cork'), ('LIMERICK', 'Limerick'), ('DUBLIN', 'Dublin'), ('WEXFORD', 'Wexford')], default='...', max_length=50),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_station',
            field=models.CharField(choices=[('DUBLIN', 'Dublin'), ('CORK', 'Cork'), ('WEXFORD', 'Wexford'), ('GALWAY', 'Galway'), ('LIMERICK', 'Limerick')], default='...', max_length=50),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=20)),
                ('transaction_id', models.CharField(max_length=50, unique=True)),
                ('total_amount', models.IntegerField(default=0)),
                ('session_key', models.CharField(max_length=50, unique=True)),
                ('card_brand', models.CharField(max_length=30)),
                ('card_type', models.CharField(max_length=50)),
                ('card_no', models.IntegerField(default=0)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busTicketBooking.reservation')),
            ],
        ),
    ]
