# Generated by Django 3.2.3 on 2023-02-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeverMissIt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='maxparticipants',
            field=models.PositiveIntegerField(verbose_name='Max. members in a Team'),
        ),
    ]