# Generated by Django 4.2.3 on 2023-07-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя и фамилия'),
        ),
    ]