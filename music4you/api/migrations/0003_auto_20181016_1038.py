# Generated by Django 2.0.7 on 2018-10-16 08:38

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181015_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='lyrics',
            field=models.FileField(blank=True, null=True, upload_to='./lyrics/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['lrc'])]),
        ),
        migrations.AlterField(
            model_name='music',
            name='upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='./mp3/320/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='music',
            name='upload_128',
            field=models.FileField(default=django.utils.timezone.now, upload_to='./mp3/128/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='music',
            name='upload_192',
            field=models.FileField(default=django.utils.timezone.now, upload_to='./mp3/192/'),
            preserve_default=False,
        ),
    ]
