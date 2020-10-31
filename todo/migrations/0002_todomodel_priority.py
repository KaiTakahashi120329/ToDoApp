# Generated by Django 3.1.2 on 2020-10-31 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('info', 'normal'), ('success', 'low')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
