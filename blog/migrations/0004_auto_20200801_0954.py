# Generated by Django 3.0.4 on 2020-08-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200801_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'DRAFT'), ('Published', 'PUBLISHED')], default='draft', max_length=10),
        ),
    ]