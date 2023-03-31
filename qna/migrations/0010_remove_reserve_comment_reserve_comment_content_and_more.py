# Generated by Django 4.1 on 2023-03-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0009_remove_reserve_comment_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='comment',
        ),
        migrations.AddField(
            model_name='reserve',
            name='comment_content',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='reserve',
            name='comment_subject',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
