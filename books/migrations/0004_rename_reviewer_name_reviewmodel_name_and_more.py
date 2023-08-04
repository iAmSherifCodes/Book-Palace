# Generated by Django 4.2.4 on 2023-08-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_reviewmodel_alter_book_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='reviewer_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='reviewmodel',
            name='date_and_time',
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='description',
            field=models.TextField(default='Enter a  Review', max_length=1200),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FICTION', 'Fiction'), ('FINANCE', 'Finance'), ('POLITICS', 'Politics'), ('ROMANCE', 'Romance')], default='Finance', max_length=10),
        ),
    ]
