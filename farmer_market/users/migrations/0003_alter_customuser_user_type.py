# Generated by Django 5.1.3 on 2024-11-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_farmer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'farmer'), (3, 'buyer')], default=3),
        ),
    ]