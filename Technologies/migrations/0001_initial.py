# Generated by Django 4.1.5 on 2023-01-28 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Technology",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=155)),
                ("index", models.IntegerField(default=1)),
            ],
        ),
    ]
