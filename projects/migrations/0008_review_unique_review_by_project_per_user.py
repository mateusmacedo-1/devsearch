# Generated by Django 5.0.6 on 2024-07-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_social_stackoverflow'),
        ('projects', '0007_alter_project_options_review_owner'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('owner', 'project'), name='unique review by project per user'),
        ),
    ]
