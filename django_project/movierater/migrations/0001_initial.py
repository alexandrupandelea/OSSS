# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('launch_date', models.IntegerField()),
                ('imdb_link', models.CharField(max_length=100)),
                ('poster', models.CharField(max_length=1000, default='https://nanohub.org/groups/bnc/Image:/equipment/missing_equip.gif')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('nr_of_people', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='grade',
            field=models.ForeignKey(to='movierater.Rating', default='0'),
        ),
    ]
