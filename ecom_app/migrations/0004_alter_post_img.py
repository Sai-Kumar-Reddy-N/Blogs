# Generated by Django 4.0.4 on 2022-05-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_post_delete_userinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static\\media'),
        ),
    ]