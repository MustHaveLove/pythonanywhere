# Generated by Django 3.2.18 on 2023-04-24 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='User_Dept',
            new_name='Emp_Dept',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='User_Name',
            new_name='Emp_Name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='User_Rank',
            new_name='Emp_Rank',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='User_User',
            new_name='Emp_User',
        ),
    ]