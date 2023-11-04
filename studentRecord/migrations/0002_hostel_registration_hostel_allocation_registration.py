# Generated by Django 4.2.6 on 2023-11-02 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentRecord', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='registration',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='studentRecord.registration'),
        ),
        migrations.AddField(
            model_name='hostel_allocation',
            name='registration',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='studentRecord.registration'),
        ),
    ]
