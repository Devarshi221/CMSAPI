# Generated by Django 4.1.7 on 2023-06-05 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Social", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post_blog",
            name="owner",
        ),
        migrations.DeleteModel(
            name="Like",
        ),
        migrations.DeleteModel(
            name="Post_blog",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
