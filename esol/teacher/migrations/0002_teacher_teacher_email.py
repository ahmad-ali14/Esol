# Generated by Django 2.1.5 on 2019-02-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_email',
            field=models.EmailField(default='teacher@mail.com', max_length=70),
            preserve_default=False,
        ),
    ]