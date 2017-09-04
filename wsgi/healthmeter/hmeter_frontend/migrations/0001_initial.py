# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 03:35
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participantinfo', '__first__'),
        ('projectinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True)),
                ('template_name', models.CharField(blank=True, default='', max_length=50)),
                ('sibling_order', models.IntegerField(blank=True, default=0)),
                ('colour', colorful.fields.RGBColorField(blank=True)),
                ('time_based', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetricAlgorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MetricCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_value', jsonfield.fields.JSONField(null=True)),
                ('score', models.FloatField()),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('is_complete', models.BooleanField()),
                ('is_dirty', models.BooleanField(default=False)),
                ('metric', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cached_scores', to='hmeter_frontend.Metric')),
            ],
        ),
        migrations.CreateModel(
            name='MetricScoreConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red_score', models.FloatField()),
                ('yellow_score', models.FloatField()),
                ('green_score', models.FloatField()),
                ('ry_boundary', models.FloatField()),
                ('yg_boundary', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Metric Score Constants instances',
                'verbose_name': 'Metric Score Constants',
            },
        ),
        migrations.CreateModel(
            name='EmailDomain',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('participantinfo.emaildomain',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
            ],
            options={
                'abstract': False,
                'indexes': [],
                'proxy': True,
            },
            bases=('projectinfo.project',),
        ),
        migrations.AddField(
            model_name='metriccache',
            name='project',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cached_scores', to='hmeter_frontend.Project'),
        ),
        migrations.AddField(
            model_name='metric',
            name='algorithm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hmeter_frontend.MetricAlgorithm'),
        ),
        migrations.AddField(
            model_name='metric',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='hmeter_frontend.Metric'),
        ),
        migrations.AlterUniqueTogether(
            name='metriccache',
            unique_together=set([('project', 'metric', 'start', 'end')]),
        ),
    ]