# Generated by Django 4.2.11 on 2024-03-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options_alter_pattern_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='description',
            field=models.CharField(default='description', max_length=200),
        ),
    ]