# Generated by Django 2.2.6 on 2019-11-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0005_auto_20191102_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='tag_id_1',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='tag_id_2',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='tag_id_3',
        ),
        migrations.AddField(
            model_name='competition',
            name='tags',
            field=models.ManyToManyField(to='flat.Tag'),
        ),
    ]
