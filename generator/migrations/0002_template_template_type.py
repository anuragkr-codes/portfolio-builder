# Generated by Django 5.2 on 2025-04-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='template_type',
            field=models.CharField(choices=[('professional_blue', 'Professional Blue'), ('modern_minimalist', 'Modern Minimalist')], default='professional_blue', max_length=50),
        ),
    ]
