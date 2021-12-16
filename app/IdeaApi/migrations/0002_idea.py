# Generated by Django 4.0 on 2021-12-13 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('ideaId', models.AutoField(primary_key=True, serialize=False)),
                ('ideaDesc', models.CharField(max_length=2000, null=True)),
                ('ideatitle', models.CharField(default='Provide a title here', max_length=200)),
                ('ideatags', models.CharField(default='#tags', max_length=200)),
                ('upVotes', models.IntegerField(null=True)),
                ('downVotes', models.IntegerField(null=True)),
                ('collaborators', models.IntegerField(null=True)),
                ('postingTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IdeaApi.user')),
            ],
        ),
    ]