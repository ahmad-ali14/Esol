# Generated by Django 2.1.5 on 2019-02-16 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_eng_classes_students_enrolled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eng_classes',
            name='students_enrolled',
        ),
    ]