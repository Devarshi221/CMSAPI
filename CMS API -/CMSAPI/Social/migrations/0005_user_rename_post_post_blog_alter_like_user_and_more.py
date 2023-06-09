# Generated by Django 4.1.7 on 2023-06-05 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Social", "0004_rename_post_blog_post_alter_like_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="user",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=50)),
                ("Password", models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name="Post",
            new_name="Post_blog",
        ),
        migrations.AlterField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Social.user"
            ),
        ),
        migrations.AlterField(
            model_name="post_blog",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Social.user"
            ),
        ),
    ]
