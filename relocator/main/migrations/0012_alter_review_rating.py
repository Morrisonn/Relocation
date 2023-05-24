# Generated by Django 4.2 on 2023-05-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.CharField(
                choices=[
                    ("1", "★"),
                    ("2", "★★"),
                    ("3", "★★★"),
                    ("4", "★★★★"),
                    ("5", "★★★★★"),
                ],
                max_length=5,
            ),
        ),
    ]
