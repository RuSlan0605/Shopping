# Generated by Django 3.2 on 2023-02-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onshop', '0004_alter_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
