# Generated by Django 5.0.3 on 2024-03-27 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.usercourse'),
        ),
    ]
