# Generated by Django 5.0.3 on 2024-03-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField(null=True)),
                ('discount', models.IntegerField(default=0, null=True)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='images/thumbnail')),
                ('resource', models.FileField(upload_to='images/resource')),
                ('length', models.IntegerField(null=True)),
            ],
        ),
    ]
