# Generated by Django 3.2.4 on 2024-09-28 09:31

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0002_follower_ux_follower_follower_followed'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follower',
            name='UX_Follower_Follower_Followed',
        ),
        migrations.AddConstraint(
            model_name='follower',
            constraint=models.UniqueConstraint(fields=('FollowingProfile', 'FollowedProfile'), name='UX_Follower_Following_Followed'),
        ),
        migrations.AddConstraint(
            model_name='follower',
            constraint=models.CheckConstraint(check=models.Q(('FollowingProfile', django.db.models.expressions.F('FollowedProfile')), _negated=True), name='CK_Follower_Following_Followed'),
        ),
    ]
