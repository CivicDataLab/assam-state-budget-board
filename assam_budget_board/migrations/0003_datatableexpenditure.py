# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-08 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('assam_budget_board', '0002_smallmultipleexpenditure'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTableExpenditure',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='assam_budget_board_datatableexpenditure', serialize=False, to='cms.CMSPlugin')),
                ('url', models.URLField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
