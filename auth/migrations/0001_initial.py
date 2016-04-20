# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('group', models.CharField(choices=[('G1', 'Group 1'), ('G2', 'Group 2'), ('G3', 'Group 3')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('group', models.ForeignKey(to='AuthConfig.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateField()),
                ('sdesc', models.CharField(max_length=60)),
                ('ldesc', models.CharField(max_length=1000)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=128)),
                ('site_manager', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(default='', max_length=128)),
                ('site_manager', models.BooleanField(default=False)),
                ('public_key', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='creator',
            field=models.ForeignKey(to='AuthConfig.User'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(to='AuthConfig.User'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='AuthConfig.User', through='AuthConfig.Membership'),
        ),
    ]
