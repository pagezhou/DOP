# Generated by Django 2.2.6 on 2021-05-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafka', '0011_auto_20210507_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kafkabroker',
            old_name='ip_port',
            new_name='ip',
        ),
        migrations.RemoveField(
            model_name='kafkacluster',
            name='brokers',
        ),
        migrations.AddField(
            model_name='kafkacluster',
            name='broker_cnt',
            field=models.IntegerField(default=0, verbose_name='broker数量'),
        ),
    ]
