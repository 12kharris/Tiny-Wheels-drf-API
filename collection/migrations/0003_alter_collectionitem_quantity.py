# Generated by Django 3.2.4 on 2024-09-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_collectionitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitem',
            name='Quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]