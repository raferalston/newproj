# Generated by Django 4.2.5 on 2023-10-09 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagemodel',
            old_name='message_datetime_notification',
            new_name='datetime_notification',
        ),
        migrations.RenameField(
            model_name='messagemodel',
            old_name='message_status',
            new_name='is_done',
        ),
        migrations.RenameField(
            model_name='messagemodel',
            old_name='message_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='messagemodel',
            old_name='message_type',
            new_name='type',
        ),
    ]
