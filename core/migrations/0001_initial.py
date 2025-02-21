# Generated by Django 5.0.7 on 2024-07-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_no', models.CharField(blank=True, max_length=100, null=True)),
                ('oil', models.IntegerField(blank=True, null=True)),
                ('gas', models.IntegerField(blank=True, null=True)),
                ('brine', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
