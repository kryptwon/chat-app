# Generated by Django 3.2.8 on 2021-10-22 12:37

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommessagemodel',
            name='message',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]