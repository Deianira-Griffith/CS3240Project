# Generated by Django 4.1.2 on 2022-11-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NewLousList", "0018_alter_shoppingcart_class_list_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="grad_year",
            field=models.IntegerField(default=2022, null=True),
        ),
    ]
