# Generated by Django 4.0.4 on 2022-04-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]