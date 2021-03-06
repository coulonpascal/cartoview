# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20160915_0944'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('short_description', models.TextField(null=True, blank=True)),
                ('app_url', models.URLField(null=True, blank=True)),
                ('author', models.CharField(max_length=200, null=True, blank=True)),
                ('author_website', models.URLField(null=True, blank=True)),
                ('license', models.CharField(max_length=200, null=True, blank=True)),
                ('date_installed', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Installed')),
                ('single_instance', models.BooleanField(default=False)),
                ('order', models.SmallIntegerField(default=0)),
                ('owner_url', models.URLField(null=True, blank=True)),
                ('help_url', models.URLField(null=True, blank=True)),
                ('is_suspended', models.NullBooleanField(default=False)),
                ('app_img_url', models.TextField(max_length=1000)),
                ('in_menu', models.NullBooleanField(default=True)),
                ('admin_only', models.NullBooleanField(default=False)),
                ('rating', models.IntegerField(default=0, null=True, blank=True)),
                ('contact_name', models.CharField(max_length=200, null=True, blank=True)),
                ('contact_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('installed_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppInstance',
            fields=[
                ('resourcebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.ResourceBase')),
                ('config', models.TextField(null=True, blank=True)),
                ('app', models.ForeignKey(blank=True, to='app_manager.App', null=True)),
                ('map', models.ForeignKey(blank=True, to='maps.Map', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.resourcebase',),
        ),
        migrations.CreateModel(
            name='AppTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, unique=True, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='tags',
            field=models.ManyToManyField(to='app_manager.AppTag', null=True, blank=True),
        ),
    ]
