# Generated by Django 4.2.5 on 2024-01-23 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tehsil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tehsil_id', models.IntegerField(unique=True)),
                ('tehsil_name', models.CharField(max_length=255)),
                ('total_num_tehsil', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uc_id', models.IntegerField(unique=True)),
                ('uc_name', models.CharField(max_length=200)),
                ('totol_num_uc', models.IntegerField()),
                ('tehsil_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rtsapp.tehsil')),
            ],
        ),
        migrations.CreateModel(
            name='VC_Hawks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vc_id', models.IntegerField()),
                ('vc_name', models.CharField(max_length=200)),
                ('total_num_vc', models.IntegerField()),
                ('uc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rtsapp.uc')),
            ],
        ),
    ]
