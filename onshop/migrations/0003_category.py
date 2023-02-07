# Generated by Django 3.2 on 2023-02-04 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onshop', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onshop.product')),
            ],
        ),
    ]