# Generated by Django 4.0.1 on 2022-01-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_genre_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='actor',
            field=models.CharField(max_length=200, verbose_name='출연'),
        ),
    ]
