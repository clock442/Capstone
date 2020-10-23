# Generated by Django 3.1.1 on 2020-10-23 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('map_image', models.ImageField(default='../uploaded_files/images/kitten1200x800.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='HoldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WallType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('height', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_leaving', models.DateTimeField(blank=True, null=True)),
                ('x_position', models.IntegerField()),
                ('y_position', models.IntegerField()),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='routeapp.gym')),
                ('hold_types', models.ManyToManyField(related_name='hold_types', to='routeapp.HoldType')),
                ('wall_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wall_type', to='routeapp.walltype')),
            ],
        ),
    ]