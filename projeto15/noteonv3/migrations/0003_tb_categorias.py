# Generated by Django 4.1.1 on 2022-10-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteonv3', '0002_alter_tb_users_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catename', models.CharField(max_length=50)),
            ],
        ),
    ]
