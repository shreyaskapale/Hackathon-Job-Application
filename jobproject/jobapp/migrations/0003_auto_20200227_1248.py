# Generated by Django 3.0.1 on 2020-02-27 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobapply', to='jobapp.ManagerProfile'),
        ),
    ]