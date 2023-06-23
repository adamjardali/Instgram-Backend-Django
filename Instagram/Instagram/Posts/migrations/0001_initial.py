# Generated by Django 4.1.9 on 2023-06-15 20:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppEffect',
            fields=[
                ('Id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('EffectName', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppFilter',
            fields=[
                ('Id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('FilterName', models.CharField(max_length=255)),
                ('FilterDetails', models.JSONField()),
            ],
            options={
                'verbose_name': 'Filter',
                'verbose_name_plural': 'Filters',
            },
        ),
        migrations.CreateModel(
            name='AppPost',
            fields=[
                ('Id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('Caption', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='AppPostMedia',
            fields=[
                ('Id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('MediaFile', models.URLField(null=True)),
                ('Position', models.IntegerField()),
                ('Longitude', models.IntegerField()),
                ('Latitude', models.IntegerField()),
                ('FilterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.appfilter')),
                ('PostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.apppost')),
            ],
            options={
                'verbose_name': 'PostMedia',
                'verbose_name_plural': 'PostsMedia',
                'unique_together': {('FilterId', 'PostId')},
            },
        ),
        migrations.CreateModel(
            name='AppPostType',
            fields=[
                ('Id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('PostTypeName', models.CharField(choices=[('PHOTO', 'PHOTO'), ('VIDEO', 'VIDEO'), ('CAROUSEL', 'CAROUSEL'), ('STORIES', 'STORIES'), ('REELS', 'REELS')], max_length=255)),
            ],
            options={
                'verbose_name': 'PostType',
                'verbose_name_plural': 'PostType',
            },
        ),
        migrations.AddField(
            model_name='apppost',
            name='PostTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.appposttype'),
        ),
        migrations.AddField(
            model_name='apppost',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.appuser'),
        ),
        migrations.CreateModel(
            name='AppPostMediaUserTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('XCoordinate', models.IntegerField()),
                ('YCoordinate', models.IntegerField()),
                ('PostMediaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.apppostmedia')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.appuser')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'unique_together': {('PostMediaId', 'UserId')},
            },
        ),
        migrations.CreateModel(
            name='AppPostEffect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateCreatedAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('Scale', models.TextField()),
                ('EffectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.appeffect')),
                ('PostMediaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.apppostmedia')),
            ],
            options={
                'verbose_name': 'PostEffect',
                'verbose_name_plural': 'PostEffects',
                'unique_together': {('EffectId', 'PostMediaId')},
            },
        ),
    ]
