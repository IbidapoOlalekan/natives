# Generated by Django 4.0.4 on 2022-04-26 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('natives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.TextField(default=())),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('natives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='natives.natives')),
            ],
        ),
    ]