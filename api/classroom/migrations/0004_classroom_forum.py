# Generated by Django 3.0 on 2020-02-07 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_comentary_forum_question'),
        ('classroom', '0003_auto_20200207_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='forum',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum'),
        ),
    ]
