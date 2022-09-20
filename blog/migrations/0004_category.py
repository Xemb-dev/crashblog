# Generated by Django 4.1.1 on 2022-09-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_options_rename_psot_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]