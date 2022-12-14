# Generated by Django 4.1.2 on 2022-10-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_guangzhi', '0003_generalscore_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_year', models.IntegerField()),
                ('grade_name', models.CharField(max_length=256)),
                ('grade_index', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=256),
        ),
    ]
