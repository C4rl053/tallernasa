# Generated by Django 2.1.3 on 2018-11-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorio',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Marca'),
            preserve_default=False,
        ),
    ]