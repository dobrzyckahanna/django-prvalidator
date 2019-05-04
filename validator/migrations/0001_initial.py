# Generated by Django 2.1.7 on 2019-05-04 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='N', max_length=1)),
                ('merged', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pr_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='N', max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='repo_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pr',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository', to='validator.Repository'),
        ),
    ]
