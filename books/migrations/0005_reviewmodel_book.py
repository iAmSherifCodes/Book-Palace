# Generated by Django 4.2.4 on 2023-08-04 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_reviewer_name_reviewmodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='books.book'),
            preserve_default=False,
        ),
    ]
