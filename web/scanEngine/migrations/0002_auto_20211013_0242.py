# Generated by Django 3.2.4 on 2021-10-13 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackerone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('api_key', models.CharField(blank=True, max_length=200, null=True)),
                ('send_critical', models.BooleanField(default=True)),
                ('send_high', models.BooleanField(default=True)),
                ('send_medium', models.BooleanField(default=False)),
                ('report_template', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_to_slack', models.BooleanField(default=False)),
                ('send_to_discord', models.BooleanField(default=False)),
                ('send_to_telegram', models.BooleanField(default=False)),
                ('slack_hook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('discord_hook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('telegram_bot_token', models.CharField(blank=True, max_length=100, null=True)),
                ('telegram_bot_chat_id', models.CharField(blank=True, max_length=100, null=True)),
                ('send_scan_status_notif', models.BooleanField(default=True)),
                ('send_interesting_notif', models.BooleanField(default=True)),
                ('send_vuln_notif', models.BooleanField(default=True)),
                ('send_subdomain_changes_notif', models.BooleanField(default=True)),
                ('send_scan_output_file', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('use_proxy', models.BooleanField(default=False)),
                ('proxies', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VulnerabilityReportSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primary_color', models.CharField(blank=True, default='#FFB74D', max_length=10, null=True)),
                ('secondary_color', models.CharField(blank=True, default='#212121', max_length=10, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_address', models.CharField(blank=True, max_length=200, null=True)),
                ('company_email', models.CharField(blank=True, max_length=100, null=True)),
                ('company_website', models.CharField(blank=True, max_length=100, null=True)),
                ('show_rengine_banner', models.BooleanField(default=True)),
                ('show_executive_summary', models.BooleanField(default=True)),
                ('executive_summary_description', models.TextField(blank=True, null=True)),
                ('show_footer', models.BooleanField(default=False)),
                ('footer_text', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='enginetype',
            name='osint',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='enginetype',
            name='screenshot',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='enginetype',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='interestinglookupmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]