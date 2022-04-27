# Generated by Django 3.2.12 on 2022-04-05 10:51

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=50, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]
