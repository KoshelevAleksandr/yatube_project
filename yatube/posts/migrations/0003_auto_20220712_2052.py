# Generated by Django 2.2.19 on 2022-07-12 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220712_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(
                  blank=True, null=True,
                  on_delete=django.db.models.deletion.CASCADE,
                  related_name='posts', to='posts.Group'),
        ),
    ]
