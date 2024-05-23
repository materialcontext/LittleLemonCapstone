# Generated by Django 5.0.4 on 2024-05-23 07:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0003_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserComments',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_date',
            new_name='bookingDate',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='reservation_slot',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]