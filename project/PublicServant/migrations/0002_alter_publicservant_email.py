# Generated by Django 4.1.3 on 2022-11-19 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('PublicServant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicservant',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='public_servants', serialize=False, to='Users.users'),
        ),
    ]