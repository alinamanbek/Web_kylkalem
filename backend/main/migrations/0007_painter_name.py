# Generated by Django 3.2.12 on 2024-04-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_paint_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='painter',
            name='name',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]