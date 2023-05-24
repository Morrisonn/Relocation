# Generated by Django 4.2 on 2023-05-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.CharField(
                choices=[
                    ("★", "1 звезда"),
                    ("★★", "2 звезды"),
                    ("★★★", "3 звезды"),
                    ("★★★★", "4 звезды"),
                    ("★★★★★", "5 звезд"),
                ],
                max_length=30,
            ),
        ),
    ]
