# Generated by Django 2.2.6 on 2021-04-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadoop', '0009_auto_20210408_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='hadooptaskrecord',
            name='task_err_result',
            field=models.TextField(default='', verbose_name='保存task错误日志'),
        ),
    ]
