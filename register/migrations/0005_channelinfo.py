# Generated by Django 3.1.2 on 2020-10-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20201020_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channelinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CannelName', models.CharField(max_length=30)),
                ('Tags', models.CharField(max_length=200)),
                ('VideoID', models.URLField()),
                ('Thumbnail', models.URLField()),
                ('Overview', models.CharField(max_length=200)),
                ('Title', models.CharField(max_length=200)),
                ('ViewCount', models.CharField(max_length=200)),
                ('likeCount', models.CharField(max_length=200)),
                ('DislikeCount', models.CharField(max_length=200)),
                ('CommentCount', models.CharField(max_length=200)),
                ('PublishedAt', models.CharField(max_length=200)),
            ],
        ),
    ]
