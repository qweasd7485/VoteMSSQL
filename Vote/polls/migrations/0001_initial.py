# Generated by Django 2.1.15 on 2021-01-15 06:39

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('revoteable', models.BooleanField(default=False)),
                ('ballot', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.IntegerField(default=0)),
                ('account', models.IntegerField(default=0)),
                ('votetimes', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 1, 15, 14, 39, 9, 141086), verbose_name='date voted')),
            ],
        ),
        migrations.CreateModel(
            name='VoteHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.IntegerField(default=0)),
                ('account', models.IntegerField(default=0)),
                ('choice', models.IntegerField(default=0)),
                ('content', models.CharField(default='', max_length=50)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 1, 15, 14, 39, 9, 142084), verbose_name='date voted')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
