# Generated by Django 2.1.5 on 2019-09-27 07:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('fld', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
            ],
        ),
    ]
