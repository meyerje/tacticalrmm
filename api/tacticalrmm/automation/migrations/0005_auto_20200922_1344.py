# Generated by Django 3.1.1 on 2020-09-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_auto_20200617_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='modified_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
