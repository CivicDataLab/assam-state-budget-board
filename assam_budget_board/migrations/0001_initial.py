# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-22 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenditureGrant',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='assam_budget_board_expendituregrant', serialize=False, to='cms.CMSPlugin')),
                ('url', models.URLField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]