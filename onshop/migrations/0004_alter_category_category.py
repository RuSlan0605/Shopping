# Generated by Django 3.2 on 2023-02-04 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onshop', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onshop.product'),
        ),
    ]
