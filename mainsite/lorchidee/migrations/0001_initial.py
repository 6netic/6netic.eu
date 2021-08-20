# Generated by Django 3.2.4 on 2021-08-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateField()),
                ('heure', models.CharField(blank=True, max_length=5, null=True)),
                ('patient', models.CharField(blank=True, max_length=65, null=True)),
                ('addrTel', models.CharField(blank=True, max_length=255, null=True)),
                ('cotation', models.CharField(blank=True, max_length=255, null=True)),
                ('assure', models.CharField(blank=True, max_length=50, null=True)),
                ('honoraire', models.CharField(blank=True, max_length=50, null=True)),
                ('finTraitement', models.CharField(blank=True, max_length=50, null=True)),
                ('commentaires', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'timeplan',
                'managed': True,
            },
        ),
    ]
