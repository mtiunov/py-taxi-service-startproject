# Generated by Django 5.0 on 2024-01-06 18:40

import django.contrib.auth.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="drivers",
            field=models.ManyToManyField(
                related_name="cars", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="taxi.manufacturer",
            ),
        ),
        migrations.AlterField(
            model_name="driver",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="driver",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]