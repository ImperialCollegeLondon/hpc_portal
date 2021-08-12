# Generated by Django 3.2.2 on 2021-08-10 20:54

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_support_oauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('script_lines', models.TextField(max_length=1000, validators=[main.validators.validate_config_lines])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='customconfig',
            name='script_lines',
            field=models.TextField(max_length=1000, validators=[main.validators.validate_config_lines]),
        ),
    ]