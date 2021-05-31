# Generated by Django 3.2.3 on 2021-05-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use $ to prefix non public channels: ex: $private_chan', max_length=120, unique=True, verbose_name='Name')),
                ('level', models.CharField(choices=[('public', 'Public'), ('users', 'Users'), ('groups', 'Groups'), ('staff', 'Staff'), ('superuser', 'Superuser')], max_length=20, verbose_name='Authorized for')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Groups')),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
            },
        ),
    ]