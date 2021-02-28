# Generated by Django 3.1 on 2021-02-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('DELETED', 'Deleted'), ('UPLOADED', 'Uploaded'), ('UPLOADING', 'Uploading'), ('NEW', 'New')], default='NEW', max_length=255),
        ),
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.CharField(choices=[('IMAGE', 'Image'), ('DOCUMENT', 'Document'), ('AUDIO', 'Audio'), ('VIDEO', 'Video'), ('PHOTO', 'Photo')], default='IMAGE', max_length=255),
        ),
        migrations.AddField(
            model_name='file',
            name='visibility',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('LIMITED', 'Limited'), ('PRIVATE', 'Private')], default='PUBLIC', max_length=255),
        ),
        migrations.AddField(
            model_name='postcontent',
            name='type',
            field=models.CharField(choices=[('LIST', 'List'), ('REVIEW', 'Review'), ('GALLERY', 'Gallery'), ('SHORT_POST', 'Short_Post'), ('NEWS', 'News'), ('EXTERNAL_RESOURCE', 'External_Resource'), ('LONG_READ', 'Long_Read')], default='SHORT_POST', max_length=30),
        ),
    ]
