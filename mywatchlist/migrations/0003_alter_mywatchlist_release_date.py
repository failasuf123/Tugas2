# Generated by Django 4.1 on 2022-09-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_mywatchlist_delete_listitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='release_date',
            field=models.TextField(),
        ),
    ]