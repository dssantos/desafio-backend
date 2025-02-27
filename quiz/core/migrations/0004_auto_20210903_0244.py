# Generated by Django 3.2.6 on 2021-09-03 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answer1',
            field=models.CharField(default='A1', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='answer2',
            field=models.CharField(default='A2', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='answer3',
            field=models.CharField(default='A3', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='right_answer',
            field=models.CharField(choices=[('A1', 'answer1'), ('A2', 'answer2'), ('A3', 'answer3')], default='A1', max_length=2),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
