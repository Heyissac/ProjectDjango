# Generated by Django 4.1.1 on 2022-09-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("andromeda", "0002_about_contactprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactprofile",
            name="number",
            field=models.CharField(max_length=12, verbose_name="Number"),
        ),
    ]
