# Generated by Django 2.2.6 on 2019-11-01 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('user_id', models.IntegerField(default=0)),
                ('competition_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='competition',
            name='like_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='competition',
            name='participate_sum',
            field=models.IntegerField(default=0),
        ),
    ]