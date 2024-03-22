# Generated by Django 4.2.11 on 2024-03-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_pattern_updated_on_alter_pattern_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='yarn',
            field=models.CharField(default='yarn', max_length=50),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='gauge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='needle_size',
            field=models.CharField(max_length=50),
        ),
    ]