# Generated by Django 3.2.5 on 2021-07-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_year_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
