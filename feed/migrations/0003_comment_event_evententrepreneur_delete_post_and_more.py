# Generated by Django 4.1 on 2022-09-10 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("entrepreneurs", "0002_alter_entrepreneur_image_profile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feed", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("direction", models.TextField()),
                ("cost_of_entry", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "image_profile",
                    models.ImageField(
                        default="images/default.jpg", upload_to="images/event_pics"
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="EventEntrepreneur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "entrepreneur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="entrepreneurs.entrepreneur",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="feed.event"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Post",
        ),
        migrations.AddField(
            model_name="comment",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="feed.event",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
