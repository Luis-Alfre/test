# Generated by Django 5.0.6 on 2024-07-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='note1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='note2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='note3',
            field=models.IntegerField(default=0),
        ),
    ]
