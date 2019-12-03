# Generated by Django 2.2.6 on 2019-10-29 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('restriction', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('participate_sum', models.IntegerField()),
                ('like_sum', models.IntegerField()),
            ],
        ),
    ]
