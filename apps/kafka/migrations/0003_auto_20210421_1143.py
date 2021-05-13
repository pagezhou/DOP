# Generated by Django 2.2.6 on 2021-04-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafka', '0002_auto_20210402_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='kafkacluster',
            name='add_type',
            field=models.IntegerField(choices=[(0, '平台录入'), (1, '平台新建')], default=1, verbose_name='集群创建方式'),
        ),
        migrations.AddField(
            model_name='kafkacluster',
            name='app_id',
            field=models.CharField(default='', max_length=100, verbose_name='业务id'),
        ),
        migrations.AddField(
            model_name='kafkacluster',
            name='cluster_status',
            field=models.IntegerField(
                choices=[
                    (0, '已下线'),
                    (1, '部署中'),
                    (2, '部署异常'),
                    (3, '上线中'),
                    (4, '集群变更中'),
                    (5, '集群异常'),
                    (6, '集群录入中'),
                    (7, '集群录入异常'),
                    (99, '未知状态'),
                ],
                default=3,
                verbose_name='集群状态',
            ),
        ),
    ]
