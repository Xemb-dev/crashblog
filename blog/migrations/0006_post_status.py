# Generated by Django 4.1.1 on 2022-09-12 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_options_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('active', 'Active')], default='active', max_length=10),
        ),
    ]
