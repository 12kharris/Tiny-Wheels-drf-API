# Generated by Django 3.2.4 on 2024-09-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_collectionitem_image'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='collectionitem',
            constraint=models.UniqueConstraint(fields=('Collection', 'Name', 'Series'), name='UX_CollectionItem_Coll_Name_Series'),
        ),
    ]
