# Generated by Django 2.2.12 on 2020-04-26 07:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2020, 4, 26, 7, 29, 52, 69875, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2020, 4, 26, 7, 29, 52, 70745, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.Post')),
            ],
        ),
    ]
