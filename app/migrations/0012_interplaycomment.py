# Generated by Django 4.2.21 on 2025-06-24 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_interplay_corruption_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterplayComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('interplay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interplay_comments', to='app.interplay')),
            ],
        ),
    ]
