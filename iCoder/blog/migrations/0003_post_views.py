# Generated by Django 5.1.2 on 2024-11-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogcomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
