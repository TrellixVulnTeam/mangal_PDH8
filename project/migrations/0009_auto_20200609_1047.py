# Generated by Django 3.2.dev20200604053612 on 2020-06-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20200607_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('soup', 'soup'), ('chicken', 'chicken'), ('lamb', 'lamb'), ('fish', 'fish'), ('vegetable', 'vegetable'), ('special', 'special'), ('child', 'child')], default='manantai', max_length=30),
        ),
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
