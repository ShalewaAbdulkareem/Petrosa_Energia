# Generated by Django 5.1.7 on 2025-03-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petrosa_energia_app', '0004_quickquote_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_name',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
