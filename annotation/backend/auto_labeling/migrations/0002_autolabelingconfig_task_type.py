# Generated by Django 3.2.11 on 2022-01-25 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auto_labeling", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="autolabelingconfig",
            name="task_type",
            field=models.CharField(
                choices=[("Category", "category"), ("Span", "span"), ("Text", "text"), ("Relation", "relation")],
                default="Category",
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]
