# Generated by Django 3.1.1 on 2020-09-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_auto_20200910_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('agent', models.CharField(blank=True, max_length=255, null=True)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(choices=[('login', 'User Login'), ('failed_login', 'Failed User Login'), ('delete', 'Delete Object'), ('modify', 'Modify Object'), ('add', 'Add Object'), ('view', 'View Object'), ('remote_session', 'Remote Session'), ('execute_script', 'Execute Script'), ('execute_command', 'Execute Command')], max_length=100)),
                ('object_type', models.CharField(choices=[('agent', 'Agent'), ('policy', 'Policy'), ('patch_policy', 'Patch Policy'), ('client', 'Client'), ('site', 'Site'), ('check', 'Check'), ('task', 'Automated Task')], max_length=100)),
                ('before_value', models.JSONField(blank=True, null=True)),
                ('after_value', models.JSONField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DebugLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
