# Generated by Django 4.0.5 on 2022-06-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxtag', '0003_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(),
        ),
    ]
