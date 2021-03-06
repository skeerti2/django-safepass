# Generated by Django 4.0.4 on 2022-05-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_list', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_domain',
            field=models.CharField(default='example.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='account_password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_username',
            field=models.CharField(max_length=50),
        ),
    ]
