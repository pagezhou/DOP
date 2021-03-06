# Generated by Django 2.2.6 on 2021-04-21 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('es', '0006_auto_20210414_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='escluster', options={'verbose_name': 'Es集群信息', 'verbose_name_plural': 'Es集群信息'},
        ),
        migrations.AlterModelOptions(
            name='esnodeinfo', options={'verbose_name': 'Es集群节点信息', 'verbose_name_plural': 'Es集群节点信息'},
        ),
        migrations.AlterModelOptions(
            name='esrule', options={'verbose_name': 'Es集群用户信息表', 'verbose_name_plural': 'Es集群用户信息表'},
        ),
        migrations.AlterUniqueTogether(name='esnodeinfo', unique_together={('cluster_name', 'ip')},),
        migrations.AlterModelTable(name='escluster', table='t_es_cluster_info',),
        migrations.AlterModelTable(name='esnodeinfo', table='t_es_cluster_detail',),
        migrations.AlterModelTable(name='esrule', table='t_es_cluster_role',),
    ]
