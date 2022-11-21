# Generated by Django 4.1.3 on 2022-11-19 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='public_servants', serialize=False, to='Users.users')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]