# Generated by Django 4.0.4 on 2022-05-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0008_rename_image_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='static\\css'),
        ),
    ]
