# Generated by Django 4.0.4 on 2022-05-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_category_category_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
