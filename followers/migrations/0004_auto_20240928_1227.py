# Generated by Django 3.2.4 on 2024-09-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_name'),
        ('followers', '0003_auto_20240928_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='FollowedProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FollowedProfile', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='FollowingProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OwningProfile', to='profiles.profile'),
        ),
    ]
