# Generated by Django 5.1.6 on 2025-03-09 16:35
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_tags"),
    ]

    operations = [TrigramExtension()]
