# Generated by Django 3.2.9 on 2022-04-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productmodel_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.TextField(blank=True, max_length=2300, null=True),
        ),
    ]
