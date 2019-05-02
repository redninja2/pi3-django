# Generated by Django 2.0.2 on 2019-05-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0012_days_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128, verbose_name='title')),
                ('info', models.CharField(default='', max_length=128, verbose_name='info')),
            ],
        ),
    ]
