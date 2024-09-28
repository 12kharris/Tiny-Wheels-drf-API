# Generated by Django 3.2.4 on 2024-09-28 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TagName', models.CharField(max_length=100)),
                ('Colour', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Title', models.CharField(max_length=100)),
                ('Caption', models.TextField(blank=True)),
                ('Image', models.ImageField(default='../default_post_e9srbd', upload_to='images/')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('Tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.tag')),
            ],
            options={
                'ordering': ['-Created_at'],
            },
        ),
    ]
