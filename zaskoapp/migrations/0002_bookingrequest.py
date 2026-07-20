# Generated manually for booking requests

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaskoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=120)),
                ('project_type', models.CharField(blank=True, max_length=120)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.TimeField()),
                ('budget', models.CharField(blank=True, max_length=120)),
                ('preferred_contact', models.CharField(default='WhatsApp', max_length=30)),
                ('message', models.TextField()),
                ('consent', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('new', 'New'), ('reviewing', 'Reviewing'), ('scheduled', 'Scheduled'), ('closed', 'Closed')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
