# Generated by Django 5.1 on 2024-08-28 18:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.IntegerField(default=0)),
                ('happy_clients', models.IntegerField(default=0)),
                ('award_wins', models.IntegerField(default=0)),
                ('countries', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Text',
            },
        ),
        migrations.CreateModel(
            name='LeftBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='left-block')),
            ],
            options={
                'verbose_name': 'Left Block',
                'verbose_name_plural': 'Left Block',
            },
        ),
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('space', models.CharField(max_length=255)),
                ('transfer', models.CharField(max_length=255)),
                ('panel', models.CharField(max_length=255)),
                ('support', models.CharField(max_length=255)),
                ('emails', models.CharField(max_length=255)),
                ('security', models.CharField(max_length=255)),
                ('is_space', models.BooleanField(default=True)),
                ('is_transfer', models.BooleanField(default=True)),
                ('is_panel', models.BooleanField(default=True)),
                ('is_support', models.BooleanField(default=True)),
                ('is_emails', models.BooleanField(default=True)),
                ('is_security', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Pricing Plan',
                'verbose_name_plural': 'Pricing Plans',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=400)),
                ('first_name', models.CharField(max_length=45)),
                ('Last_name', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='reviews')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='RightBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='right-block')),
            ],
            options={
                'verbose_name': 'Right Block',
                'verbose_name_plural': 'Right Block',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('html_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
        migrations.CreateModel(
            name='TreeBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='tree-blocks')),
            ],
            options={
                'verbose_name': 'Tree Block',
                'verbose_name_plural': 'Tree Blocks',
            },
        ),
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='work_process')),
            ],
            options={
                'verbose_name': 'Work process',
                'verbose_name_plural': 'Work process',
            },
        ),
    ]
