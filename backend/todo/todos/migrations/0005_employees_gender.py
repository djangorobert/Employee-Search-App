# Generated by Django 2.0.6 on 2018-06-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_employees_hired'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True),
        ),
    ]