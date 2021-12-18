# Generated by Django 4.0 on 2021-12-17 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaApi', '0003_alter_idea_user_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default=None, max_length=300)),
                ('ideaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IdeaApi.idea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IdeaApi.user')),
            ],
        ),
    ]
