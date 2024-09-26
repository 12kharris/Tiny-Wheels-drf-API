# Generated by Django 3.2.4 on 2024-09-26 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FollowedProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_profile', to='profiles.profile')),
                ('FollowingProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owning_profile', to='profiles.profile')),
            ],
        ),
    ]
